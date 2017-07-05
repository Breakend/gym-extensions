import os.path as osp
import tempfile
import xml.etree.ElementTree as ET
import math

import numpy as np

import gym
import random
import os
from gym import utils
from gym.envs.mujoco import mujoco_env

import pyrr
from pyrr.utils import all_parameters_as_numpy_arrays
import math
import six

def isclose(a, b, rel_tol=1e-04, abs_tol=0.0):
    # TODO: move to util func
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

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


def WallEnvFactory(class_type):
    """class_type should be an OpenAI gym time"""

    class WallEnv(class_type, utils.EzPickle):
        # Using https://github.com/bstadie/third_person_im/blob/88516c1703221586099062053af696f0b4a31cda/rllab/envs/mujoco/maze/maze_env.py
        # as a base
        # ORI_IND = None

        # TODO: remove this
        MAZE_MAKE_CONTACTS = False

        # manually give a penalty if the torso comes into contact with the wall
        MANUAL_COLLISION = False
        # TODO: this suckssssss, maye shouldn't use mujoco at all.

        def __init__(
                self,
                model_path,
                ori_ind,
                wall_height = .25,
                wall_pos_range = ([1.8, 0.0], [3.8, 0.0]),
                n_bins=10,
                sensor_range=10.,
                sensor_span=math.pi/2,
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
            wall_readings = np.zeros(self._n_bins)
            # goal_readings = np.zeros(self._n_bins)

            for ray_idx in range(self._n_bins):
                theta = (self._sensor_span/self._n_bins)*ray_idx - self._sensor_span/2.   # self._sensor_span * 0.5 + 1.0 * (2 * ray_idx + 1) / (2 * self._n_bins) * self._sensor_span
                forward_normal = rotate_vector(np.array([1,0,0]), [0,1,0], theta)
                # Note: Mujoco quaternions use [w, x, y, z] convention
                quat_mujoco = self.get_body_xquat("torso")
                quat = [quat_mujoco[1], quat_mujoco[2], quat_mujoco[3], quat_mujoco[0]]
                ray_direction = pyrr.quaternion.apply_to_vector(quat, forward_normal)
                ray = pyrr.ray.create(robot_coords, ray_direction)

                bottom_point = [self.wall_pos[0] - self.wall_size[0]/2.,
                                self.wall_pos[1] - self.wall_size[1]/2.,
                                0.]
                top_point = [self.wall_pos[0] + self.wall_size[0]/2.,
                                self.wall_pos[1] + self.wall_size[1]/2.,
                                self.wall_size[2]]

                # import pdb; pdb.set_trace()
                bounding_box = pyrr.aabb.create_from_points([bottom_point, top_point])
                intersection = pyrr.geometric_tests.ray_intersect_aabb(ray, bounding_box)

                if intersection is not None:
                    distance = np.linalg.norm(intersection - robot_coords)
                    if distance <= self._sensor_range:
                        wall_readings[ray_idx] = distance / self._sensor_range

            obs = np.concatenate([
                self.class_type._get_obs(self),
                wall_readings
                # goal_readings
            ])
            # print("wall readings:", wall_readings)
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
                if self._is_in_collision(new_pos):
                    # print("Collision " + new_pos)
                    reward = -10.0
            else:
                state, reward, done, info = super(WallEnv, self)._step(action)

            next_obs = self._get_obs()

            x, y = self.get_body_com("torso")[:2]
            return next_obs, reward, done, info

        def action_from_key(self, key):
            return self.action_from_key(key)
    return WallEnv
