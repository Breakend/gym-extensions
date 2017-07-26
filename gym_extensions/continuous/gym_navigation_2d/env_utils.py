import scipy
from scipy import stats
import numpy as np
from math import sqrt, asin, cos, sin, atan2, ceil
import networkx as nx
import sys
import pickle

from .geometry_utils import *

class Obstacle(object):
    def __init__(self, c, w, h):

        if type(c) == type([]):
            self.rectangle_centers = c
            self.rectangle_widths = w
            self.rectangle_heights = h

            assert(c)

            self.lowest_point = np.array([ c[0][0], c[0][1] - h[0]/2.0])
            self.representative_point = c[0].copy()

            for ca, wa, ha in zip(c, w, h):
                if (self.lowest_point[1] > ca[1] - ha/2.0):
                    self.lowest_point = np.array([ca[0], ca[1] - ha/2.0])

        else:
            self.rectangle_centers = [c]
            self.rectangle_widths = [w]
            self.rectangle_heights = [h]
            self.lowest_point = np.array([c[0], c[1] - h/2.0])
            self.representative_point = c.copy()

    def __eq__(self, other):
        return all([ (sc == oc).all() for sc, oc in zip(self.rectangle_centers, other.rectangle_centers) ])  and \
            all([ (sw == ow).all() for sw, ow in zip(self.rectangle_widths, other.rectangle_widths) ]) and \
            all([ (sh == oh).all() for sh, oh in zip(self.rectangle_heights, other.rectangle_heights) ])

    def append(self, ca, wa, ha):
        self.rectangle_centers.append(ca)
        self.rectangle_widths.append(wa)
        self.rectangle_heights.append(ha)

        if (self.lowest_point[1] > ca[1] - ha/2.0):
            self.lowest_point = np.array([ca[0], ca[1] - ha/2.0])

    def merge(self, obs):
        self.rectangle_centers.extend(obs.rectangle_centers)
        self.rectangle_widths.extend(obs.rectangle_widths)
        self.rectangle_heights.extend(obs.rectangle_heights)

        for ca, wa, ha in zip(obs.rectangle_centers, obs.rectangle_widths, obs.rectangle_heights):
            if (self.lowest_point[1] > ca[1] - ha/2.0):
                self.lowest_point = np.array([ca[0], ca[1] - ha/2.0])

    def distance_to_point(self, x, y):
        p = np.array([x,y])
        dist = [point_to_rectangle_distance(p, ca, wa, ha) for ca,wa,ha in zip(self.rectangle_centers, self.rectangle_widths, self.rectangle_heights)]
        return min(dist)

    def distance_to_rectangle(self, ca, wa, ha):
        dist = [rectangle_to_rectangle_distance(ca, cb, wa, wb, ha, hb) for cb,wb,hb in zip(self.rectangle_centers, self.rectangle_widths, self.rectangle_heights)]
        return min(dist)

    def distance_to_obstacle(self, obs):
        dist = [self.distance_to_rectangle(ca, wa, ha) for ca,wa,ha in zip(obs.rectangle_centers, obs.rectangle_widths, obs.rectangle_heights)]
        return min(dist)

    def closest_point_to(self, p):
        closest_points_to_segments = [closest_point_on_segment(p, s, t) for c,w,h in zip(self.rectangle_centers, self.rectangle_widths, self.rectangle_heights) \
                                      for s,t in rectangle_edges( np.array([c[0] + w/2.0, c[1] + h/2.0]), \
                                                                  np.array([c[0] + w/2.0, c[1] - h/2.0]), \
                                                                  np.array([c[0] - w/2.0, c[1] - h/2.0]), \
                                                                  np.array([c[0] - w/2.0, c[1] + h/2.0]) )]

        distances = [np.linalg.norm(p - cp) for cp in closest_points_to_segments]
        idx = np.argmin(distances)

        return closest_points_to_segments[idx]

class Environment(object):
    def __init__(self, x_range, y_range, obstacles):
        self.obstacles = obstacles
        self.x_range = x_range
        self.y_range = y_range

        w = x_range[1] - x_range[0]
        h = y_range[1] - y_range[0]

        self.image = 255*np.ones((h, w, 3), dtype='uint8')
        for obs in self.obstacles:
            for co, wo, ho in zip(obs.rectangle_centers, obs.rectangle_widths, obs.rectangle_heights):
                r = co[1]
                c = co[0]
                min_row = max(int(r - ho/2.0), 0)
                max_row = min(int(r + ho/2.0), h-1)

                min_col = max(int(c - wo/2.0), 0)
                max_col = min(int(c + wo/2.0), w-1)

                self.image[min_row:max_row, min_col:max_col, :] = (204, 153, 102)


    def __eq__(self, other):
        return self.obstacles == other.obstacles and self.x_range == other.x_range and self.y_range == other.y_range

    def point_distance_from_obstacles(self, x, y):
        dist = [obs.distance_to_point(x, y) for obs in self.obstacles]
        return min(dist)


    def point_is_in_free_space(self, x, y, epsilon=0.25):
        row = int(y)
        col = int(x)

        if (row >=0 and row < self.image.shape[0] and col >= 0 and col < self.image.shape[1]):
            return (self.image[row, col, :] == (255, 255, 255)).all()
        else:
            return True


    def range_and_bearing_to_closest_obstacle(self, x,y):
        dist = [(self.obstacles[i].distance_to_point(x, y), i) for i in range(len(self.obstacles))]
        distance_to_closest_obstacle, idx_closest = min(dist)
        closest_obstacle = self.obstacles[idx_closest]
        cp = closest_obstacle.closest_point_to(np.array([x,y]))
        bearing_to_closest_obstacle = atan2(cp[1]-y, cp[0]-x)
        return distance_to_closest_obstacle, bearing_to_closest_obstacle


    def segment_is_in_free_space(self, x1,y1, x2,y2, epsilon=0.5):
        # Note: this is assuming that 1px = 1m
        a = np.array([x1,y1])
        b = np.array([x2,y2])
        L = np.linalg.norm(b-a)
        return all([self.point_is_in_free_space(a[0] + i/L*(b[0]-a[0]), a[1] + i/L*(b[1]-a[1])) for i in range(ceil(L))])


    def segment_distance_from_obstacles(self, x1, y1, x2, y2):

        if not self.segment_is_in_free_space(x1, y1, x2, y2, epsilon=1e-10):
            return 0.0

        a = np.array([x1, y1])
        b = np.array([x2, y2])

        dist = [point_to_segment_distance(p, a, b) for obs in self.obstacles \
                for c,w,h in zip(obs.rectangle_centers, obs.rectangle_widths, obs.rectangle_heights) for p in rectangle_vertices(c,w,h)]

        return min(dist)

    def raytrace(self, p, theta, max_range, n_evals=50):
        """TODO: implement a less naive collision algo than this"""
        ct = cos(theta)
        st = sin(theta)
        direction = np.array([ct, st])

        a = p
        b = p + max_range * direction

        if self.segment_is_in_free_space(a[0], a[1], b[0], b[1], epsilon=1e-10):
            return -1.0

        last_free_dist = 0
        for e in range(n_evals):
            dist = e/float(n_evals) * max_range
            c = a + dist * direction
            if not self.point_is_in_free_space(c[0], c[1], epsilon=1e-10):
                return last_free_dist

            last_free_dist = dist
        return max_range

    def winding_angle(self, path, point):
        wa = 0
        for i in range(len(path)-1):
            p = np.array([path[i].x, path[i].y])
            pn = np.array([path[i+1].x, path[i+1].y])

            vp = p - point
            vpn = pn - point

            vp_norm = sqrt(vp[0]**2 + vp[1]**2)
            vpn_norm = sqrt(vpn[0]**2 + vpn[1]**2)

            assert (vp_norm > 0)
            assert (vpn_norm > 0)

            z = np.cross(vp, vpn)/(vp_norm * vpn_norm)
            z = min(max(z, -1.0), 1.0)
            wa += asin(z)

        return wa

    def homology_vector(self, path):
        L = len(self.obstacles)
        h = np.zeros((L, 1) )
        for i in range(L):
            h[i, 0] = self.winding_angle(path, self.obstacles[i].representative_point)

        return h.reshape((L,))
