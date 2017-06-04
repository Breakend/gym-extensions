import os.path as osp
import tempfile
import xml.etree.ElementTree as ET
import math

import numpy as np

from rllab import spaces
from rllab.envs.base import Step
from rllab.envs.proxy_env import ProxyEnv

from rllab.misc.overrides import overrides
from rllab.envs.mujoco.maze.maze_env_utils import ray_segment_intersect, point_distance
import gym
import random
import os
from gym import utils
from gym.envs.mujoco import mujoco_env
from pyrr.utils import all_parameters_as_numpy_arrays
import pyrr

def isclose(a, b, rel_tol=1e-04, abs_tol=0.0):
    # TODO: move to util func
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

import math

def rotate_vector(v, axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis/math.sqrt(np.dot(axis, axis))
    a = math.cos(theta/2.0)
    b, c, d = -axis*math.sin(theta/2.0)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    R = np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                     [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                     [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])

    return np.dot(R, v)

@all_parameters_as_numpy_arrays
def ray_intersect_aabb(ray, aabb):
    """Calculates the intersection point of a ray and an AABB
    :param numpy.array ray1: The ray to check.
    :param numpy.array aabb: The Axis-Aligned Bounding Box to check against.
    :rtype: numpy.array
    :return: Returns a vector if an intersection occurs.
        Returns None if no intersection occurs.
    """
    """
    http://gamedev.stackexchange.com/questions/18436/most-efficient-aabb-vs-ray-collision-algorithms
    """
    # this is basically "numpy.divide( 1.0, ray[ 1 ] )"
    # except we're trying to avoid a divide by zero warning
    # so where the ray direction value is 0.0, just use infinity
    # which is what we want anyway
    direction = ray[1]
    dir_fraction = np.empty(3, dtype = ray.dtype)
    dir_fraction[direction == 0.0] = np.inf
    dir_fraction[direction != 0.0] = np.divide(1.0, direction[direction != 0.0])

    t1 = (aabb[0,0] - ray[0,0]) * dir_fraction[ 0 ]
    t2 = (aabb[1,0] - ray[0,0]) * dir_fraction[ 0 ]
    t3 = (aabb[0,1] - ray[0,1]) * dir_fraction[ 1 ]
    t4 = (aabb[1,1] - ray[0,1]) * dir_fraction[ 1 ]
    t5 = (aabb[0,2] - ray[0,2]) * dir_fraction[ 2 ]
    t6 = (aabb[1,2] - ray[0,2]) * dir_fraction[ 2 ]


    tmin = max(min(t1, t2), min(t3, t4), min(t5, t6))
    tmax = min(max(t1, t2), max(t3, t4), max(t5, t6))

    # if tmax < 0, ray (line) is intersecting AABB
    # but the whole AABB is behind the ray start
    if tmax < 0:
        return None, None

    # if tmin > tmax, ray doesn't intersect AABB
    if tmin > tmax:
        return None, None

    # t is the distance from the ray point
    # to intersection

    t = abs(tmin)
    point = ray[0] + (ray[1] * t)
    return point, t

def quaternion_multiply(quaternion1, quaternion0):
    """Return multiplication of two quaternions.

    >>> q = quaternion_multiply([4, 1, -2, 3], [8, -5, 6, 7])
    >>> numpy.allclose(q, [28, -44, -14, 48])
    True

    """
    w0, x0, y0, z0 = quaternion0
    w1, x1, y1, z1 = quaternion1
    return np.array([
        -x1*x0 - y1*y0 - z1*z0 + w1*w0,
        x1*w0 + y1*z0 - z1*y0 + w1*x0,
        -x1*z0 + y1*w0 + z1*x0 + w1*y0,
        x1*y0 - y1*x0 + z1*w0 + w1*z0], dtype=np.float64)

def quaternion_conjugate(quaternion):
    """Return conjugate of quaternion.

    >>> q0 = random_quaternion()
    >>> q1 = quaternion_conjugate(q0)
    >>> q1[0] == q0[0] and all(q1[1:] == -q0[1:])
    True

    """
    q = np.array(quaternion, dtype=np.float64, copy=True)
    np.negative(q[1:], q[1:])
    return q


def unit_vector(data, axis=None, out=None):
    """Return ndarray normalized by length, i.e. Euclidean norm, along axis.

    >>> v0 = numpy.random.random(3)
    >>> v1 = unit_vector(v0)
    >>> numpy.allclose(v1, v0 / numpy.linalg.norm(v0))
    True
    >>> v0 = numpy.random.rand(5, 4, 3)
    >>> v1 = unit_vector(v0, axis=-1)
    >>> v2 = v0 / numpy.expand_dims(numpy.sqrt(numpy.sum(v0*v0, axis=2)), 2)
    >>> numpy.allclose(v1, v2)
    True
    >>> v1 = unit_vector(v0, axis=1)
    >>> v2 = v0 / numpy.expand_dims(numpy.sqrt(numpy.sum(v0*v0, axis=1)), 1)
    >>> numpy.allclose(v1, v2)
    True
    >>> v1 = numpy.empty((5, 4, 3))
    >>> unit_vector(v0, axis=1, out=v1)
    >>> numpy.allclose(v1, v2)
    True
    >>> list(unit_vector([]))
    []
    >>> list(unit_vector([1]))
    [1.0]

    """
    if out is None:
        data = np.array(data, dtype=np.float64, copy=True)
        if data.ndim == 1:
            data /= math.sqrt(np.dot(data, data))
            return data
    else:
        if out is not data:
            out[:] = np.array(data, copy=False)
        data = out
    length = np.atleast_1d(np.sum(data*data, axis))
    np.sqrt(length, length)
    if axis is not None:
        length = np.expand_dims(length, axis)
    data /= length
    if out is None:
        return data

# rotate vector v1 by quaternion q1
def qv_mult(q1, v1):
    v1 = unit_vector(v1)
    q2 = list(v1)
    q2.append(0.0)
    return quaternion_multiply(
        quaternion_multiply(q1, q2),
        quaternion_conjugate(q1)
    )[:3]


def WallEnvFactory(class_type):
    """class_type should be an OpenAI gym time"""

    class WallEnv(class_type, utils.EzPickle):
        # Using https://github.com/bstadie/third_person_im/blob/88516c1703221586099062053af696f0b4a31cda/rllab/envs/mujoco/maze/maze_env.py
        # as a base
        # ORI_IND = None

        # TODO: remove this
        MAZE_MAKE_CONTACTS = False

        # manually give a penalty if the torso comes into contact with the wall
        MANUAL_COLLISION = True
        # TODO: this suckssssss, maye shouldn't use mujoco at all.

        def __init__(
                self,
                model_path,
                ori_ind,
                wall_height = .25,
                wall_pos_range = ([1.8, 0.0], [3.8, 0.0]),
                n_bins=5,
                sensor_range=10.,
                sensor_span=math.pi/4,
                *args,
                **kwargs):

            self._n_bins = n_bins
            self.ori_ind = ori_ind
            # Add a sensor
            self._sensor_range = sensor_range
            self._sensor_span = sensor_span

            # model_path = os.path.dirname(gym.envs.mujoco.__file__) + "/assets/" + xml_name
            # model_path = osp.join(MODEL_DIR, path)
            tree = ET.parse(model_path)
            worldbody = tree.find(".//worldbody")

            height = wall_height
            self.wall_pos_range = wall_pos_range
            rand_x = random.uniform(wall_pos_range[0][0], wall_pos_range[1][0]) #self.np_random.uniform(low=wall_pos_range[0][0], high=wall_pos_range[1][0], size=1)[0]
            rand_y = random.uniform(wall_pos_range[0][1], wall_pos_range[1][1]) #self.np_random.uniform(low=wall_pos_range[0][1], high=wall_pos_range[1][1], size=1)[0]
            self.wall_pos = wall_pos = (rand_x, rand_y)
            torso_x, torso_y = 0, 0
            self._init_torso_x = torso_x
            self.class_type = class_type
            self._init_torso_y = torso_y
            self.wall_size = (0.2, 0.4, height)

            ET.SubElement(
                worldbody, "geom",
                name="wall",
                pos="%f %f %f" % (wall_pos[0],
                                  wall_pos[1],
                                  height / 2.),
                size="%f %f %f" % self.wall_size,
                type="box",
                material="",
                contype="1",
                conaffinity="1",
                density="0.00001",
                rgba="1.0 0. 1. 1"
            )

            torso = tree.find(".//body[@name='torso']")
            geoms = torso.findall(".//geom")
            for geom in geoms:
                if 'name' not in geom.attrib:
                    raise Exception("Every geom of the torso must have a name "
                                    "defined")

            if self.__class__.MAZE_MAKE_CONTACTS:
                contact = ET.SubElement(
                    tree.find("."), "contact"
                )

                for geom in geoms:
                    ET.SubElement(
                        contact, "pair",
                        geom1=geom.attrib["name"],
                        geom2="wall"
                    )

            _, file_path = tempfile.mkstemp(text=True)
            tree.write(file_path)

            # self._goal_range = self._find_goal_range()
            self._cached_segments = None

            class_type.__init__(self, model_path=file_path)
            utils.EzPickle.__init__(self)

            # import pdb; pdb.set_trace()

        def get_body_xquat(self, body_name):
            import six
            idx = self.model.body_names.index(six.b(body_name))
            return self.model.data.xquat[idx]

        def _reset(self):
            temp = np.copy(self.model.geom_pos)

            rand_x = random.uniform(self.wall_pos_range[0][0], self.wall_pos_range[1][0])
            rand_y = random.uniform(self.wall_pos_range[0][1], self.wall_pos_range[1][1])

            # TODO: make this more robust,
            # hardcoding that the second geom is the wall,
            # but we should do something more robust??
            assert isclose(temp[1][0], self.wall_pos[0])
            assert isclose(temp[1][1],self.wall_pos[1])

            self.wall_pos = wall_pos = (rand_x, rand_y)

            temp[1][0] = self.wall_pos[0]
            temp[1][1] = self.wall_pos[1]
            self.model.geom_pos = temp
            self.model._compute_subtree()
            self.model.forward()
            ob = super(WallEnv, self)._reset()
            return ob

        def _get_obs(self):
            # The observation would include both information about the robot itself as well as the sensors around its
            # environment
            robot_x, robot_y, robot_z = robot_coords = self.get_body_com("torso")
            # print(robot_coords)
            # if self.ori_ind < 0:
            #     # forward facing vector
            #     forward_normal = np.array([0,1,0])
            #     ray_direction = qv_mult(self.get_body_xquat("torso"), forward_normal)
            #     ray = pyrr.ray.create(robot_coords, ray_direction)
            #     bottom_point = (self.wall_pos[0] - self.wall_size[0]/2.,
            #                     self.wall_pos[1] - self.wall_size[1]/2.,
            #                     0.)
            #     top_point = (self.wall_pos[0] + self.wall_size[0]/2.,
            #                     self.wall_pos[1] + self.wall_size[1]/2.,
            #                     self.wall_size[2])
            #
            #     bounding_box = pyrr.aabb.create_from_points(bottom_point, top_point)
            #     intersection, distance = ray_intersect_aabb(ray, bounding_box)
            # else:
            #     ori = self.model.data.qpos[self.ori_ind]
            # import pdb; pdb.set_trace()

            # print ori
            segments = []
            # compute the distance of all segments

            # Get all line segments of the goal and the obstacles

            # cx = self.wall_pos[0] - self._init_torso_x
            # cy = self.wall_pos[1] - self._init_torso_y
            # x1 = cx - 0.5
            # x2 = cx + 0.5
            # y1 = cy - 0.5
            # y2 = cy + 0.5
            # struct_segments = [
            #     ((x1, y1), (x2, y1)),
            #     ((x2, y1), (x2, y2)),
            #     ((x2, y2), (x1, y2)),
            #     ((x1, y2), (x1, y1)),
            # ]
            #
            # for seg in struct_segments:
            #     segments.append(dict(
            #         segment=seg,
            #         type=1,
            #     ))

            wall_readings = np.zeros(self._n_bins)
            # goal_readings = np.zeros(self._n_bins)

            for ray_idx in range(self._n_bins):
                # import pdb; pdb.set_trace()
                theta = (self._sensor_span/self._n_bins)*ray_idx - self._sensor_span/2.   # self._sensor_span * 0.5 + 1.0 * (2 * ray_idx + 1) / (2 * self._n_bins) * self._sensor_span
                # print(theta)
                # forward_normal = rotate_vector(np.array([-1,0,0]), [0,1,0], theta)
                # print(forward_normal)

                quat = self.get_body_xquat("torso")
                ray_direction = quat[:3]#qv_mult(quat, forward_normal)
                ray_direction = rotate_vector(ray_direction, [0,1,0], theta)
                print(ray_direction)
                ray = pyrr.ray.create(robot_coords, ray_direction)
                bottom_point = [self.wall_pos[0] - self.wall_size[0]/2.,
                                self.wall_pos[1] - self.wall_size[1]/2.,
                                0.]
                top_point = [self.wall_pos[0] + self.wall_size[0]/2.,
                                self.wall_pos[1] + self.wall_size[1]/2.,
                                self.wall_size[2]]

                # import pdb; pdb.set_trace()
                bounding_box = pyrr.aabb.create_from_points([bottom_point, top_point])
                intersection, distance = ray_intersect_aabb(ray, bounding_box)
                # ray_ori = ori - self._sensor_span * 0.5 + 1.0 * (2 * ray_idx + 1) / (2 * self._n_bins) * self._sensor_span
                # ray_segments = []
                # for seg in segments:
                #     p = ray_segment_intersect(ray=((robot_x, robot_y), ray_ori), segment=seg["segment"])
                #     if p is not None:
                #         ray_segments.append(dict(
                #             segment=seg["segment"],
                #             type=seg["type"],
                #             ray_ori=ray_ori,
                #             distance=point_distance(p, (robot_x, robot_y)),
                #         ))
                if distance is not None and distance <= self._sensor_range:
                    # print(distance)
                    wall_readings[ray_idx] = distance / self._sensor_range
                # if len(ray_segments) > 0:
                #     first_seg = sorted(ray_segments, key=lambda x: x["distance"])[0]
                #     # print first_seg
                #     if first_seg["type"] == 1:
                #         # Wall -> add to wall readings
                #         if first_seg["distance"] <= self._sensor_range:
                #             wall_readings[ray_idx] = (self._sensor_range - first_seg["distance"]) / self._sensor_range
                #     # elif first_seg["type"] == 'g':
                #     #     # Goal -> add to goal readings
                #     #     if first_seg["distance"] <= self._sensor_range:
                #     #         goal_readings[ray_idx] = (self._sensor_range - first_seg["distance"]) / self._sensor_range
                #     else:
                #         assert False

            obs = np.concatenate([
                self.class_type._get_obs(self),
                wall_readings
                # goal_readings
            ])
            # print "wall readings:", wall_readings
            # print "goal readings:", goal_readings

            return obs

        def _is_in_collision(self, pos):
            x, y = pos

            minx = self.wall_pos[0] * 1 - 1 * 0.5 - self._init_torso_x
            maxx = self.wall_pos[0] * 1 + 1 * 0.5 - self._init_torso_x
            miny = self.wall_pos[1] * 1 - 1 * 0.5 - self._init_torso_y
            maxy = self.wall_pos[1] * 1 + 1 * 0.5 - self._init_torso_y
            if minx <= x <= maxx and miny <= y <= maxy:
                return True
            return False


        def get_xy(self):
            return self.get_body_com("torso")[:2]

        def _step(self, action):
            # import pdb; pdb.set_trace()
            if self.MANUAL_COLLISION:
                old_pos = self.get_xy()
                state, reward, done, info = super(WallEnv, self)._step(action)
                new_pos = self.get_xy()
                # print(new_pos)
                if self._is_in_collision(new_pos):
                    # print("Collision " + new_pos)
                    reward = -10.0
            else:
                state, reward, done, info = super(WallEnv, self)._step(action)

            next_obs = self._get_obs()

            x, y = self.get_body_com("torso")[:2]
            # ref_x = x + self._init_torso_x
            # ref_y = y + self._init_torso_y
            # reward = 0
            # minx, maxx, miny, maxy = self._goal_range
            # print "goal range: x [%s,%s], y [%s,%s], now [%s,%s]" % (str(minx), str(maxx), str(miny), str(maxy),
            #                                                          str(x), str(y))
            # if minx <= x <= maxx and miny <= y <= maxy:
            #     done = True
            #     reward = 1
            return Step(next_obs, reward, done, **info)

        def action_from_key(self, key):
            return self.action_from_key(key)
    return WallEnv
