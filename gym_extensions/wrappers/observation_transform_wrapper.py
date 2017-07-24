import numpy as np
from gym import Env, spaces

from cached_property import cached_property

from .proxy_env import ProxyEnv
from .serializable import Serializable

BIG = 1e6

class ObservationTransformWrapper(ProxyEnv, Serializable):
    ''' Runs observation through a set of transforms and adjusts the observation space accordingly.'''

    def __init__(self, env, transformers):
        '''
        :param env: the environment
        :param transformers: a list of transformers
        '''
        Serializable.quick_init(self, locals())
        self.transformers = transformers
        super(ObservationTransformWrapper, self).__init__(env)

    @cached_property
    def observation_space(self):
        obs_space = self._wrapped_env.observation_space
        print("Original observation space : {}".format(obs_space))
        for transformer in self.transformers:
            obs_space = transformer.transformed_observation_space(obs_space)
        print("Transformed observation space : {}".format(obs_space))
        return obs_space

    def reset(self):
        obs = self._wrapped_env.reset()
        for transformer in self.transformers:
            obs = transformer.transform(obs)
            transformer.reset()
        return obs

    def step(self, action):
        next_obs, reward, done, info = self._wrapped_env.step(action)
        for transformer in self.transformers:
            next_obs = transformer.transform(next_obs)
        return (next_obs, reward, done, info)
