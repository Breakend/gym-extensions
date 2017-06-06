import gym
from gym import error, spaces, utils
from gym.utils import seeding
from .env_generator import Environment, EnvironmentCollection
from gym.envs.classic_control import rendering
from gym.spaces import Box, Tuple

from .range_based_navigation import StateBasedMDPNavigation2DEnv
from math import pi, cos, sin
import numpy as np
import cv2


class ImageBasedNavigation2DEnv(StateBasedMDPNavigation2DEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self, *args, **kwargs):
        StateBasedMDPNavigation2DEnv.__init__(self, *args, **kwargs)
        self.observation_space = Box(0., 255., self.world.image.shape)

    def _get_observation(self, state):
        image = self.world.image.copy()

        state_col = int(self.state[0])
        state_row = (self.world.image.shape[0] - 1) - int(self.state[1])

        dest_col = int(self.destination[0])
        dest_row = (self.world.image.shape[0] - 1) - int(self.destination[1])

        cv2.circle(image, center=(state_col, state_row), radius=5, color=(0,0,0), thickness=-1)
        cv2.circle(image, center=(dest_col, dest_row), radius=int(self.destination_tolerance_range), color=(255,0,0), thickness=-1)

        return image
