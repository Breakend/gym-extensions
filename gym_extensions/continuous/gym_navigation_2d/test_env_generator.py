import unittest
import numpy as np
from env_generator import EnvironmentCollection, EnvironmentGenerator
from env_utils import Environment
from geometry_utils import *

from math import sqrt
import os

class TestDistanceMethods(unittest.TestCase):

    def test_point_to_segment(self):
        p = np.array([0,0])
        a = np.array([1,1])
        b = np.array([2,2])
        self.assertEqual(point_to_segment_distance(p,a,b), sqrt(2))


    def test_point_to_segment2(self):
        p = np.array([3,3])
        a = np.array([1,1])
        b = np.array([2,2])
        self.assertEqual(point_to_segment_distance(p,a,b), sqrt(2))


    def test_point_to_segment3(self):
        p = np.array([1.5,1.5])
        a = np.array([1,1])
        b = np.array([2,2])
        self.assertEqual(point_to_segment_distance(p,a,b), 0.)


    def test_point_to_segment4(self):
        p = np.array([1,0])
        a = np.array([1,1])
        b = np.array([2,2])
        self.assertEqual(point_to_segment_distance(p,a,b), 1)


    def test_point_to_rectangle_distance(self):
        p = np.array([0, 0])
        c = np.array([1, 1])
        w = 1.0
        h = 1.0
        self.assertEqual(point_to_rectangle_distance(p, c, w, h), sqrt(2*(0.5)**2))


    def test_point_to_rectangle_distance2(self):
        p = np.array([1, 1])
        c = np.array([1, 1])
        w = 1.0
        h = 1.0
        self.assertEqual(point_to_rectangle_distance(p, c, w, h), 0)

    def test_point_to_rectangle_distance3(self):
        p = np.array([0.6, 0.6])
        c = np.array([1, 1])
        w = 1.0
        h = 1.0
        self.assertEqual(point_to_rectangle_distance(p, c, w, h), 0)

        p = np.array([1.4, 1.4])
        c = np.array([1, 1])
        w = 1.0
        h = 1.0
        self.assertEqual(point_to_rectangle_distance(p, c, w, h), 0)


    def test_rectangle_to_rectangle_distance(self):
        ca = np.array([1, 1])
        wa = 1.0
        ha = 1.0

        cb = np.array([0, 0])
        wb = 1.0
        hb = 1.0

        self.assertEqual(rectangle_to_rectangle_distance(ca, cb, wa, wb, ha, hb), 0)


    def test_rectangle_to_rectangle_distance2(self):
        ca = np.array([0, 2])
        wa = 2.0
        ha = 2.0

        cb = np.array([0, 0])
        wb = 1.0
        hb = 1.0

        self.assertEqual(rectangle_to_rectangle_distance(ca, cb, wa, wb, ha, hb), 0.5)


    def test_rectangle_to_rectangle_distance3(self):
        ca = np.array([0, 2])
        wa = 2.0
        ha = 2.0

        cb = np.array([0, 0])
        wb = 1.0
        hb = 1.0

        self.assertEqual(rectangle_to_rectangle_distance(ca, cb, wa, wb, ha, hb), 0.5)


    def test_rectangle_to_rectangle_distance4(self):
        ca = np.array([0, 0])
        wa = 2.0
        ha = 2.0

        cb = np.array([0, 0])
        wb = 1.0
        hb = 1.0

        self.assertEqual(rectangle_to_rectangle_distance(ca, cb, wa, wb, ha, hb), 0.)


    def test_rectangle_to_rectangle_distance5(self):
        ca = np.array([-1, 0])
        wa = 1.0
        ha = 1.0

        cb = np.array([0, 0])
        wb = 1.0
        hb = 1.0

        self.assertEqual(rectangle_to_rectangle_distance(ca, cb, wa, wb, ha, hb), 0.)


    def test_rectangle_to_rectangle_distance6(self):
        ca = np.array([-2, 0])
        wa = 1.0
        ha = 1.0

        cb = np.array([0, 0])
        wb = 1.0
        hb = 1.0

        self.assertEqual(rectangle_to_rectangle_distance(ca, cb, wa, wb, ha, hb), 1.)


    def test_rectangle_to_rectangle_distance7(self):
        ca = np.array([-2, -2])
        wa = 1.0
        ha = 1.0

        cb = np.array([0, 0])
        wb = 1.0
        hb = 1.0

        self.assertEqual(rectangle_to_rectangle_distance(ca, cb, wa, wb, ha, hb), sqrt(8) - 2*sqrt(2*0.5**2))

    def test_rectangle_to_rectangle_distance8(self):
        ca = np.array([45.41472479,  42.0288299])
        wa = 1.63125936059
        ha = 6.08773739678

        cb = np.array([45.70077727,  41.39116316])
        wb = 6.98818845647
        hb = 3.83908874358

        self.assertEqual(rectangle_to_rectangle_distance(ca, cb, wa, wb, ha, hb), 0)


    def test_rectangle_to_object_distance(self):
        ca = np.array([-2, -2])
        wa = 1.0
        ha = 1.0

        obs = Obstacle(ca,wa,ha)

        cb = np.array([0, 0])
        wb = 1.0
        hb = 1.0

        self.assertEqual(obs.distance_to_rectangle(cb, wb, hb), sqrt(8) - 2*sqrt(2*0.5**2))


    def test_rectangle_to_object_distance2(self):
        ca = np.array([-2, -2])
        wa = 1.0
        ha = 1.0
        obs = Obstacle(ca,wa,ha)

        obs.append(np.array([2,2]), 1, 1)

        cb = np.array([0, 0])
        wb = 1.0
        hb = 1.0

        self.assertEqual(obs.distance_to_rectangle(cb, wb, hb), sqrt(8) - 2*sqrt(2*0.5**2))


    def test_rectangle_to_object_distance3(self):
        ca = np.array([-2, -2])
        wa = 1.0
        ha = 1.0
        obs = Obstacle(ca,wa,ha)

        obs.append(np.array([2,2]), 1, 1)
        obs.append(np.array([1,1]), 1, 1)

        cb = np.array([0, 0])
        wb = 1.0
        hb = 1.0

        self.assertEqual(obs.distance_to_rectangle(cb, wb, hb), 0)


    def test_object_to_object_distance(self):
        ca = np.array([-2, -2])
        wa = 1.0
        ha = 1.0
        obs = Obstacle(ca,wa,ha)
        obs.append(np.array([2,2]), 1, 1)
        obs.append(np.array([1,1]), 1, 1)

        cb = np.array([0, 0])
        wb = 1.0
        hb = 1.0
        obs2 = Obstacle(cb,wb,hb)

        self.assertEqual(obs.distance_to_obstacle(obs2), 0)


    def test_object_to_object_distance2(self):
        ca = np.array([-2, -2])
        wa = 1.0
        ha = 1.0
        obs = Obstacle(ca,wa,ha)
        obs.append(np.array([2,2]), 1, 1)
        obs.append(np.array([1,1]), 1, 1)

        cb = np.array([4, 2])
        wb = 1.0
        hb = 1.0
        obs2 = Obstacle(cb,wb,hb)
        obs2.append(np.array([1,1]), 1, 1)

        self.assertEqual(obs.distance_to_obstacle(obs2), 0)


    def test_object_to_object_distance3(self):
        ca = np.array([-2, -2])
        wa = 1.0
        ha = 1.0
        obs = Obstacle(ca,wa,ha)
        obs.append(np.array([2,2]), 1, 1)
        obs.append(np.array([1,1]), 1, 1)

        cb = np.array([4, 2])
        wb = 1.0
        hb = 1.0
        obs2 = Obstacle(cb,wb,hb)
        obs2.append(np.array([10,10]), 1, 1)
        obs2.append(np.array([0,2.1]), 1, 1)

        self.assertAlmostEqual(obs.distance_to_obstacle(obs2), 0.1)


    def test_merge_rectangles(self):
        centers = np.array([[-2,-2], [2,2], [0,0], [10,10], [11,11]])
        widths = np.array([2,2,2,1,1]).reshape((len(centers),1))
        heights = np.array([2,2,2,1,1]).reshape((len(centers),1))


        eg = EnvironmentGenerator([0, 50], [0, 50], [1,5], [1, 5])
        obstacles = eg.merge_rectangles_into_obstacles(centers, widths, heights, epsilon=0.2)

        self.assertEqual(len(obstacles), 2)


    def test_merge_rectangles2(self):
        centers = np.array([[-2,-2], [2,2], [0,0], [11,11], [10,10]])
        widths = np.array([2,2,2,1,1]).reshape((len(centers),1))
        heights = np.array([2,2,2,1,1]).reshape((len(centers),1))

        eg = EnvironmentGenerator([0, 50], [0, 50], [1,5], [1, 5])
        obstacles = eg.merge_rectangles_into_obstacles(centers, widths, heights, epsilon=0.2)

        self.assertEqual(len(obstacles), 2)


    def test_merge_rectangles3(self):
        centers = np.array([[-2,-2], [2,2], [0,0], [10,10], [12,12], [11,11]])
        widths = np.array([2,2,2,1,1,1]).reshape((len(centers),1))
        heights = np.array([2,2,2,1,1,1]).reshape((len(centers),1))

        eg = EnvironmentGenerator([0, 50], [0, 50], [1,5], [1, 5])
        obstacles = eg.merge_rectangles_into_obstacles(centers, widths, heights, epsilon=0.2)

        self.assertEqual(len(obstacles), 2)

    def test_merge_rectangles4(self):
        centers = np.array([[-2,-2], [2,2], [0,0], [10,10], [13,13], [11,11], [12,12]])
        widths = np.array([2,2,2,1,1,1,1]).reshape((len(centers),1))
        heights = np.array([2,2,2,1,1,1,1]).reshape((len(centers),1))

        eg = EnvironmentGenerator([0, 50], [0, 50], [1,5], [1, 5])
        obstacles = eg.merge_rectangles_into_obstacles(centers, widths, heights, epsilon=0.2)

        self.assertEqual(len(obstacles), 2)


    def test_merge_rectangles5(self):
        centers = np.array([[-2,-2], [2,2], [0,0], [10,10], [13,13], [12,12]])
        widths = np.array([2,2,2,1,1,1]).reshape((len(centers),1))
        heights = np.array([2,2,2,1,1,1]).reshape((len(centers),1))

        eg = EnvironmentGenerator([0, 50], [0, 50], [1,5], [1, 5])
        obstacles = eg.merge_rectangles_into_obstacles(centers, widths, heights, epsilon=0.2)

        self.assertEqual(len(obstacles), 3)


    def test_point_in_free_space(self):
        centers = np.array([[0,0]])
        widths = np.array([10]).reshape((len(centers),1))
        heights = np.array([10]).reshape((len(centers),1))

        eg = EnvironmentGenerator([0, 50], [0, 50], [1,5], [1, 5])
        obstacles = eg.merge_rectangles_into_obstacles(centers, widths, heights, epsilon=0.2)

        env = Environment(eg.x_range, eg.y_range, list(obstacles.values()))

        self.assertTrue(env.point_is_in_free_space(6,6))
        self.assertTrue(env.point_is_in_free_space(5,5))

        self.assertFalse(env.point_is_in_free_space(4,4))
        self.assertFalse(env.point_is_in_free_space(0.5,0.5))

        self.assertTrue(env.point_is_in_free_space(-4,-4))
        self.assertTrue(env.point_is_in_free_space(-5,-5))
        self.assertTrue(env.point_is_in_free_space(-6,-6))


    def test_segment_in_free_space(self):
        centers = np.array([[0,0]])
        widths = np.array([10]).reshape((len(centers),1))
        heights = np.array([10]).reshape((len(centers),1))

        eg = EnvironmentGenerator([0, 50], [0, 50], [1,5], [1, 5])
        obstacles = eg.merge_rectangles_into_obstacles(centers, widths, heights, epsilon=0.2)

        env = Environment(eg.x_range, eg.y_range, list(obstacles.values()))

        self.assertFalse(env.segment_is_in_free_space(-5, 1, 5, 1))
        self.assertTrue(env.segment_is_in_free_space(-5,-4, 5, -4))


    def test_save_read(self):
        centers = np.array([[4,4], [10,10]])
        widths = np.array([1,1]).reshape((len(centers),1))
        heights = np.array([3,3]).reshape((len(centers),1))

        eg = EnvironmentGenerator([0, 100], [0, 100], [1,5], [1, 5])
        obstacles = eg.merge_rectangles_into_obstacles(centers, widths, heights, epsilon=0.2)

        env = Environment(eg.x_range, eg.y_range, list(obstacles.values()))

        centers2 = np.array([[5,5], [10,10]])
        widths2 = np.array([1,1]).reshape((len(centers2),1))
        heights2 = np.array([2,2]).reshape((len(centers2),1))

        eg2 = EnvironmentGenerator([0, 100], [0, 100], [1,5], [1, 5])
        obstacles2 = eg2.merge_rectangles_into_obstacles(centers2, widths2, heights2, epsilon=0.2)

        env2 = Environment(eg2.x_range, eg2.y_range, list(obstacles2.values()))

        ec = EnvironmentCollection()
        ec.x_range = [0, 100]
        ec.y_range = [0, 100]
        ec.width_range = [1,5]
        ec.height_range = [1,5]
        ec.num_environments = 0
        ec.map_collection = {0: env, 1: env2}

        ec.save('./temp.pkl')

        ec2 = EnvironmentCollection()
        ec2.read('./temp.pkl')

        self.assertEqual(ec2.x_range, ec.x_range)
        self.assertEqual(ec2.y_range, ec.y_range)
        self.assertEqual(ec2.map_collection, ec.map_collection)

        os.remove('./temp.pkl')


if __name__ == '__main__':
    unittest.main()
