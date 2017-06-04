import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
import os.path as osp
from gym_extensions.continuous.wall_envs import WallEnvFactory
from rllab.core.serializable import Serializable
from gym.envs.mujoco.hopper import HopperEnv

import os
import gym
HopperWallEnv = lambda *args, **kwargs : WallEnvFactory(HopperWithSensorEnv)(xml_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/hopper.xml", ori_ind=-1, *args, **kwargs)


class ModifiedHopperEnv(HopperEnv, utils.EzPickle):
    def __init__(self, **kwargs):
        # import pdb; pdb.set_trace()
        # abs_path =
        mujoco_env.MujocoEnv.__init__(self, osp.abspath(osp.join(osp.dirname(__file__), '.')) + "/mujoco_xmls/" + kwargs["xml_name"], 4)
        # mujoco_env.MujocoEnv.__init__(self, kwargs["xml_path"], 4)
        utils.EzPickle.__init__(self)

class HopperWithSensorEnv(HopperEnv, utils.EzPickle):
    def __init__(self, n_bins=5, **kwargs):
        # import pdb; pdb.set_trace()
        # abs_path = osp.abspath(osp.join(osp.dirname(__file__), '.'))
        # mujoco_env.MujocoEnv.__init__(self, abs_path + "/mujoco_xmls/" + kwargs["xml_name"], 4)
        self.n_bins = n_bins
        mujoco_env.MujocoEnv.__init__(self, kwargs["xml_path"], 4)
        utils.EzPickle.__init__(self)


    def _get_obs(self):
        obs = np.concatenate([
            HopperEnv._get_obs(self),
            np.zeros(self.n_bins)
            # goal_readings
        ])
        return obs
