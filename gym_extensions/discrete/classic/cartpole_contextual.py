"""
Classic cart-pole system implemented by Rich Sutton et al.
Copied from https://webdocs.cs.ualberta.ca/~sutton/book/code/pole.c
"""

import logging
import math
import gym
from gym import spaces
from gym.envs.classic_control.cartpole import CartPoleEnv
from gym.utils import seeding
import numpy as np

logger = logging.getLogger(__name__)

def register_custom_cartpole(tag, gravity=9.8, masscart=1.0, masspole=0.1, pole_length=.5, force_mag=10.0):
    """
    Tag - What to call your env (e.g. CustomCartpoleLongPole-v0, CustomCartpoleLongPole-v1)
    gravity - if you want to modify the gravity factor (default 9.8)
    masscart - the mass of the cartpole base
    masspole - the mass of the pole
    length - the length of the pole
    force_mag - the magnitude of the exerted action force
    """
    return gym.envs.register(
        id=tag,
        entry_point="envs.transfer.classic.cartpole_contextual:CartPoleContextualEnv",
        max_episode_steps=200,
        reward_threshold=195.0,
        kwargs= dict(gravity = gravity, masscart = masscart, masspole = masspole, length = pole_length, force_mag = force_mag)
    )

class CartPoleContextualEnv(CartPoleEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second' : 50
    }

    def __init__(self,gravity=9.8, masscart=1.0, masspole=0.1, length = .5, force_mag = 10.0):
        super(CartPoleContextualEnv, self).__init__()
        self.context   = [masscart, masspole, length, force_mag]
        self.gravity   = gravity # not including in the context for now
        self.masscart  = self.context[0]
        self.masspole  = self.context[1]
        self.length    = self.context[2]
        self.force_mag = self.context[3]
        
        # our own responsibility to define the range of the context, since we define it
        context_high = np.array([
            self.masscart  * 2,
            self.masspole  * 10,
            self.length    * 2,
            self.force_mag * 2])
        
        context_low = np.array([ 0.1, 0.1, 0.1, 0.1]) # the params in the context can't be less or equal to zero!

        self.context_space = spaces.Box(context_low, context_high)


    def _step(self, action):
        state, reward, done, _  = super(CartPoleContextualEnv, self)._step(action)
        return state, reward, done, {'masscart':self.masscart, 'masspole':self.masspole, 'pole_length':self.length, 'force_magnitude':self.force_mag}


    def change_context(self, context_vector):
        self.context = context_vector
        self.masscart  = self.context[0]
        self.masspole  = self.context[1]
        self.length    = self.context[2]
        self.force_mag = self.context[3]
