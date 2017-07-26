#!/usr/bin/python

import scipy
from scipy import stats
import numpy as np
from math import sqrt, asin, cos, sin, atan2
import networkx as nx
from .env_utils import Obstacle, Environment
from .geometry_utils import *
import sys
import pickle


class EnvironmentGenerator(object):

    def __init__(self, x_range, y_range, width_range, height_range):
        self.x_range = x_range
        self.y_range = y_range
        self.width_range = width_range
        self.height_range = height_range

    def sample_spatial_poisson_process(self, rate):
        xmin, xmax = self.x_range
        ymin, ymax = self.y_range

        dx = xmax - xmin
        dy = ymax - ymin

        N = stats.poisson( rate * dx * dy ).rvs()
        x = stats.uniform.rvs(xmin, dx, ((N, 1)) )
        y = stats.uniform.rvs(ymin, dy, ((N, 1)) )

        centers = np.hstack((x,y))
        return centers

    def sample_axis_aligned_rectangles(self, density):
        wmin, wmax = self.width_range
        hmin, hmax = self.height_range

        dw = wmax - wmin
        dh = hmax - hmin

        centers = self.sample_spatial_poisson_process(rate=density)
        widths = stats.uniform.rvs(wmin, dw, ((centers.shape[0], 1)) )
        heights = stats.uniform.rvs(hmin, dh, ((centers.shape[0], 1)) )

        # Only keep obstacels that are fully within allowed range
        # This is so that pixel occupancy queries are the same as
        # continuous distance queries, if they are ever used
        x_within_bounds = centers[:, 0] + widths[:, 0]/2.0 <= x_range[1]
        x_within_bounds = x_within_bounds * (centers[:, 0] - widths[:, 0]/2.0 >= x_range[0])

        y_within_bounds = centers[:, 1] + heights[:, 0]/2.0 <= y_range[1]
        y_within_bounds = y_within_bounds * (centers[:, 1] - heights[:, 0]/2.0 >= y_range[0])

        valid_idx = x_within_bounds * y_within_bounds
        return centers[valid_idx, :], widths[valid_idx, :], heights[valid_idx, :]

    def merge_rectangles_into_obstacles(self, centers, widths, heights, epsilon):
        """Merges rectangles defined by centers, widths, heights. Two rectangles
        with distance < epsilon are considered part of the same object."""

        G = nx.Graph()
        obstacles = {i: Obstacle(centers[i, :], widths[i, 0], heights[i, 0]) for i in range(len(centers))}
        G.add_nodes_from(obstacles.keys())

        for i in obstacles:
            for j in obstacles:
                if i != j and obstacles[i].distance_to_obstacle(obstacles[j]) < epsilon:
                    G.add_edge(i,j)

        merged_obstacles = {}
        conn_components = nx.connected_components(G)
        for cc in conn_components:
            cc = list(cc)
            new_obs = obstacles[cc[0]]
            for i in range(1, len(cc)):
                new_obs.merge(obstacles[cc[i]])

            merged_obstacles[cc[0]] = new_obs

        return merged_obstacles


class EnvironmentCollection(object):

    def __init__(self):
        self.x_range = []
        self.y_range = []
        self.width_range = []
        self.height_range = []
        self.num_environments = 0
        self.map_collection = {}

    def generate_random(self, x_range, y_range, width_range, height_range, density, num_environments):
        self.x_range = x_range
        self.y_range = y_range
        self.width_range = width_range
        self.height_range = height_range
        self.num_environments = num_environments
        self.map_collection = {}

        eg = EnvironmentGenerator(x_range, y_range, width_range, height_range)
        for i in range(self.num_environments):
            print('Sampling environment', i)
            centers, widths, heights = eg.sample_axis_aligned_rectangles(density)
            obstacles = eg.merge_rectangles_into_obstacles(centers, widths, heights, epsilon=0.2)
            self.map_collection[i] = Environment(self.x_range, self.y_range, list(obstacles.values()))

    def read(self, pkl_filename):
        file_object = open(pkl_filename, 'rb')
        self.x_range, self.y_range, worlds_without_classes = pickle.load(file_object, encoding='bytes')
        self.map_collection = {idx: Environment(val[0], val[1], [Obstacle(c,w,h) for c,w,h in val[2]]) for idx, val in worlds_without_classes.items()}
        file_object.close()

    def save(self, pkl_filename):
        file_object = open(pkl_filename, 'wb')
        worlds_without_classes = { idx : (world.x_range,
                                          world.y_range,
                                        [(obs.rectangle_centers, obs.rectangle_widths, obs.rectangle_heights)  for obs in world.obstacles])

                                   for idx, world in self.map_collection.items()}

        pickle.dump((self.x_range, self.y_range, worlds_without_classes), file_object)
        file_object.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath_to_save", help="The pickle filepath (i.e. assets/world_640x480_v0.pkl)")
    parser.add_argument("--num_environments", default=10, type=int)
    args = parser.parse_args()

    x_range=[0, 640]
    y_range=[0, 480]
    width_range=[10, 30]
    height_range=[10,50]

    density = 0.0003

    ec = EnvironmentCollection()
    ec.generate_random(x_range, y_range, width_range, height_range, density, args.num_environments)
    ec.save(args.filepath_to_save)
