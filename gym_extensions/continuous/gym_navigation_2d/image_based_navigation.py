import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym.spaces import Box, Tuple

from math import pi, cos, sin
import numpy as np
import logging 
from skimage.draw import circle
from skimage.transform import resize
from .range_based_navigation import StateBasedMDPNavigation2DEnv

class ImageBasedNavigation2DEnv(StateBasedMDPNavigation2DEnv):
    logger = logging.getLogger(__name__)
    metadata = {'render.modes': ['human']}

    def __init__(self, *args, **kwargs):
        StateBasedMDPNavigation2DEnv.__init__(self, *args, **kwargs)
        self.obs_img_shape = (160, 120, 3)
        
        self.observation_space = Box(0., 255., (self.obs_img_shape[1], self.obs_img_shape[0], 3))

    def set_circular_observation(self, img, col_center, row_center, radius, color=(0,0,0)):
        rr,cc = circle(row_center, col_center, radius)
        # make sure within bounds of img
        rr[rr<0] = 0
        rr[rr>img.shape[0]-1] = img.shape[0]-1
        cc[cc<0] = 0
        cc[cc>img.shape[1]-1] = img.shape[1]-1
        img[rr,cc] = color
        return img

    def _get_observation(self, state):
        image = self.world.image.copy()

        state_col = int(self.state[0])
        state_row = int(self.state[1])

        dest_col = int(self.destination[0])
        dest_row = int(self.destination[1])
        dest_rad = int(self.destination_tolerance_range)
        image = self.set_circular_observation(image, state_col, state_row, 5, (0,0,0))
        image = self.set_circular_observation(image, dest_col, dest_row, dest_rad, (255,0,0))
        image = image[::-1,:,:]
        image = resize(image, self.obs_img_shape[0:2][::-1])

        return image
