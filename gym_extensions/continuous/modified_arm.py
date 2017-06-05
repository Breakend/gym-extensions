import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
import os.path as osp
from rllab.core.serializable import Serializable
from gym_extensions.continuous.gravity_envs import GravityEnvFactory
from gym.envs.mujoco.pusher import PusherEnv

import os
import gym

ArmGravityEnv = lambda *args, **kwargs : GravityEnvFactory(ModifiedArmEnv)(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/pusher.xml", *args, **kwargs)


class ModifiedArmEnv(PusherEnv, utils.EzPickle):
    """
    Simply allows changing of XML file, probably not necessary if we pull request the xml name as a kwarg in openai gym
    """
    def __init__(self, **kwargs):
        mujoco_env.MujocoEnv.__init__(self, kwargs["model_path"], 5)
        utils.EzPickle.__init__(self)

        
