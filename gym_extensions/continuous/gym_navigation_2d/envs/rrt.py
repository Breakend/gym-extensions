#!/usr/bin/python
import sys
import time
import pickle
import numpy as np
import random

from itertools import product
from math import cos, sin, pi, sqrt 
import copy

class State(object):
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.children = []
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def euclidean_distance(self, state):
        assert (state)
        return sqrt((state.x - self.x)**2 + (state.y - self.y)**2)

    
class RRT(object):
    def __init__(self, world):
        self.world = world
        
    def state_is_free(self, state):
        return self.world.point_is_in_free_space(state.x, state.y, epsilon=0.2) 
    
    def sample_state(self):
        x = random.uniform(self.world.x_range[0], self.world.x_range[1])
        y = random.uniform(self.world.y_range[0], self.world.y_range[1])
        return State(x, y, None)
           

    def _follow_parent_pointers(self, state):
        """
        Returns the path [start_state, ..., destination_state] by following the
        parent pointers.
        """
        
        curr_ptr = state
        path = [state]
        
        while curr_ptr is not None:
            path.append(curr_ptr)
            curr_ptr = curr_ptr.parent

        # return a reverse copy of the path (so that first state is starting state)
        return path[::-1]


    def find_closest_state(self, tree_nodes, state):
        min_dist = float("Inf")
        closest_state = None
        for node in tree_nodes:
            dist = node.euclidean_distance(state)  
            if dist < min_dist:
                closest_state = node
                min_dist = dist

        return closest_state

    def steer_towards(self, s_nearest, s_rand, max_radius):
        """
        Returns a new state s_new whose coordinates x and y
        are decided as follows:
        
        If s_rand is within a circle of max_radius from s_nearest
        then s_new.x = s_rand.x and s_new.y = s_rand.y
        
        Otherwise, s_rand is farther than max_radius from s_nearest. 
        In this case we place s_new on the line from s_nearest to
        s_rand, at a distance of max_radius away from s_nearest.
        
        """

        vx = float(s_rand.x - s_nearest.x)
        vy = float(s_rand.y - s_nearest.y)
        v  = sqrt(vx**2 + vy**2)
        
        x = 0
        y = 0
        
        if v < max_radius:
            x = s_rand.x
            y = s_rand.y            
        elif v > 1e-10:
            x = s_nearest.x + vx/v * max_radius
            y = s_nearest.y + vy/v * max_radius
        
        s_new = State(x, y, s_nearest)
        return s_new


    def segment_is_obstacle_free(self, s_from, s_to):
        """
        Returns true iff the line path from s_from to s_to
        is free
        """
        assert (self.state_is_free(s_from))
        
        if not (self.state_is_free(s_to)):
            return False

        return self.world.segment_is_in_free_space(s_from.x, s_from.y, s_to.x, s_to.y)

    
    def plan(self, start_state, dest_state, max_num_steps, max_steering_radius, dest_reached_radius):
        """
        Returns a path as a sequence of states [start_state, ..., dest_state]
        if dest_state is reachable from start_state. Otherwise returns [start_state].
        Assume both source and destination are in free space.
        """
        assert (self.state_is_free(start_state))
        assert (self.state_is_free(dest_state))

        # The set containing the nodes of the tree
        tree_nodes = set()
        tree_nodes.add(start_state)
        
        # image to be used to display the tree
        img = np.copy(self.world)

        plan = [start_state]
        
        for step in xrange(max_num_steps):

            s_rand = self.sample_state()
            s_nearest = self.find_closest_state(tree_nodes, s_rand)
            s_new = self.steer_towards(s_nearest, s_rand, max_steering_radius)
            
            if self.segment_is_obstacle_free(s_nearest, s_new):
                tree_nodes.add(s_new)
                s_nearest.children.append(s_new)

                # If we approach the destination within a few pixels
                # we're done. Return the path.
                if s_new.euclidean_distance(dest_state) < dest_reached_radius:
                    dest_state.parent = s_new
                    plan = self._follow_parent_pointers(dest_state)
                    return plan, tree_nodes
                
        return [start_state], tree_nodes

    def smooth(self, path, alpha=1.5, rate=0.01, max_iterations=400, min_safe_distance=1.5):
        path = copy.deepcopy(path)
        old_path = np.array([ [state.x, state.y] for state in path])
        new_path = old_path.copy()
        it = 0
        
        while True:
            
            gradE = (new_path - old_path) 
            for i in xrange(1, len(path)-1):
                gradE[i, :] -= alpha*(new_path[i+1, :] + new_path[i-1, :] - 2*new_path[i, :])

            gradE[0, :] = 0
            gradE[-1, :] = 0

            proposed_new_path = new_path -  rate*gradE
            
            safe_idx = [self.world.segment_is_in_free_space(proposed_new_path[i-1][0],
                                                            proposed_new_path[i-1][1],
                                                            proposed_new_path[i][0],
                                                            proposed_new_path[i][1]) and \
                                           
                        self.world.segment_is_in_free_space(proposed_new_path[i][0],
                                                            proposed_new_path[i][1],
                                                            proposed_new_path[i+1][0],
                                                            proposed_new_path[i+1][1]) \
                          
                        for i in xrange(1, proposed_new_path.shape[0]-1)]


            improving_idx = [self.world.segment_distance_from_obstacles(proposed_new_path[i][0],
                                                                        proposed_new_path[i][1],
                                                                        proposed_new_path[i+1][0],
                                                                        proposed_new_path[i+1][1]) >

                             self.world.segment_distance_from_obstacles(old_path[i][0],
                                                                        old_path[i][1],
                                                                        old_path[i+1][0],
                                                                        old_path[i+1][1])
                             
                             for i in xrange(1, proposed_new_path.shape[0]-1)]

            safe_idx = np.array([False] + safe_idx + [False])
            improving_idx = np.array([False] + improving_idx + [False])
            safe_idx = safe_idx + improving_idx
            
            if not (any(safe_idx) and it < max_iterations):
                break
            
            new_path[safe_idx, :] = proposed_new_path[safe_idx, :]
            it += 1

        for i in xrange(1, len(path)-1):
            path[i].x = new_path[i, 0]
            path[i].y = new_path[i, 1]

        return path
