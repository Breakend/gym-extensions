import numpy as np

from gym import spaces
from .proxy_env import ProxyEnv
from gym.spaces.box import Box


class NormalizedEnv(ProxyEnv):
    def __init__(
            self,
            env,
            normalize_obs=False,
            obs_alpha=0.001,
    ):
        ProxyEnv.__init__(self, env)
        self._normalize_obs = normalize_obs
        self._obs_alpha = obs_alpha
        self._obs_mean = np.zeros(env.observation_space.flat_dim)
        self._obs_var = np.ones(env.observation_space.flat_dim)


    def _update_obs_estimate(self, obs):
        flat_obs = self.wrapped_env.observation_space.flatten(obs)
        self._obs_mean = (1 - self._obs_alpha) * self._obs_mean + self._obs_alpha * flat_obs
        self._obs_var = (1 - self._obs_alpha) * self._obs_var + self._obs_alpha * np.square(flat_obs - self._obs_mean)

    def _apply_normalize_obs(self, obs):
        self._update_obs_estimate(obs)
        return (obs - self._obs_mean) / (np.sqrt(self._obs_var) + 1e-8)

    def reset(self):
        ret = self._wrapped_env.reset()
        if self._normalize_obs:
            return self._apply_normalize_obs(ret)
        else:
            return ret

    @property
    @overrides
    def action_space(self):
        if isinstance(self._wrapped_env.action_space, Box):
            ub = np.ones(self._wrapped_env.action_space.shape)
            return spaces.Box(-1 * ub, ub)
        return self._wrapped_env.action_space

    @overrides
    def step(self, action):
        if isinstance(self._wrapped_env.action_space, Box):
            # rescale the action
            lb, ub = self._wrapped_env.action_space.bounds
            scaled_action = lb + (action + 1.) * 0.5 * (ub - lb)
            scaled_action = np.clip(scaled_action, lb, ub)
        else:
            scaled_action = action
        wrapped_step = self._wrapped_env.step(scaled_action)
        next_obs, reward, done, info = wrapped_step
        if self._normalize_obs:
            next_obs = self._apply_normalize_obs(next_obs)
        return next_obs, reward, done, info

    def __str__(self):
        return "Normalized: %s" % self._wrapped_env

    # def log_diagnostics(self, paths):
    #     print "Obs mean:", self._obs_mean
    #     print "Obs std:", np.sqrt(self._obs_var)
    #     print "Reward mean:", self._reward_mean
    #     print "Reward std:", np.sqrt(self._reward_var)

normalize = NormalizedEnv
