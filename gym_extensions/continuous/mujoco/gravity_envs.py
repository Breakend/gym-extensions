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
import mujoco_py

def GravityEnvFactory(class_type):
    """class_type should be an OpenAI gym type"""

    class GravityEnv(class_type, utils.EzPickle):
        """
        Allows the gravity to be changed by the
        """
        def __init__(
                self,
                model_path,
                gravity=-9.81,
                *args,
                **kwargs):
            class_type.__init__(self, model_path=model_path)
            utils.EzPickle.__init__(self)

            # make sure we're using a proper OpenAI gym Mujoco Env
            assert isinstance(self, mujoco_env.MujocoEnv)

            self.model.opt.gravity = (mujoco_py.mjtypes.c_double * 3)(*[0., 0., gravity])
            self.model._compute_subtree()
            self.model.forward()

    return GravityEnv
