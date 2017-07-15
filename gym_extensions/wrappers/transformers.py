import numpy as np
import scipy.misc
from gym.spaces.box import Box
from scipy.misc import imresize

from cached_property import cached_property


# TODO: move this to folder with different files

class BaseTransformer(object):
    """
    Base transformer interface, inherited objects should conform to this
    """

    def transform(self, observation):
        """
        observation to transform
        """
        raise NotImplementedError

    def transformed_observation_space(self, prev_observation_space):
        """
        prev_observation_space and how it is modified
        """
        return prev_observation_space

    def reset(self):
        """
        resets the transformer if there is an operation to be made
        """
        return

class AppendPrevTimeStepTransformer(BaseTransformer):
    """
    Keeps track of and appends the previous observation timestep.
    """
    def __init__(self):
        self.prev_timestep = None

    def transform(self, observation):
        if self.prev_timestep is None:
            self.prev_timestep = np.zeros(observation.shape)

        new_obs = np.concatenate([observation.reshape((1, -1)), self.prev_timestep.reshape((1, -1))], axis=1).reshape(-1)

        self.prev_timestep = observation
        return new_obs

    def transformed_observation_space(self, prev_observation_space):
        if type(prev_observation_space) is Box:
            #TODO: should use tile?
            copy = np.copy(prev_observation_space.low.reshape((1, -1)))
            low = np.concatenate([copy, copy], axis=1)
            copy = np.copy(prev_observation_space.high.reshape((1, -1)))
            high = np.concatenate([copy, copy], axis=1)
            return Box(low.reshape(-1), high.reshape(-1))
        else:
            raise NotImplementedError("Currently only support Box observation spaces for ResizeImageTransformer")

        return prev_observation_space

    def reset(self):
        self.prev_timestep = None

class SimpleNormalizePixelIntensitiesTransformer(BaseTransformer):
    """
    Normalizes pixel intensities simply by dividing by 255.
    """
    def transform(self, observation):
        return np.array(observation).astype(np.float32) / 255.0

    def transformed_observation_space(self, wrapped_observation_space):
        return wrapped_observation_space

class ResizeImageTransformer(BaseTransformer):
    """
    Rescale a given image by a percentage
    """

    def __init__(self, fraction_of_current_size):
        self.fraction_of_current_size = fraction_of_current_size

    def transform(self, observation):
        return scipy.misc.imresize(observation, self.fraction_of_current_size)

    def transformed_observation_space(self, wrapped_observation_space):
        if type(wrapped_observation_space) is Box:
            return Box(scipy.misc.imresize(wrapped_observation_space.low, self.fraction_of_current_size), scipy.misc.imresize(wrapped_observation_space.high, self.fraction_of_current_size))
        else:
            raise NotImplementedError("Currently only support Box observation spaces for ResizeImageTransformer")

class RandomSensorMaskTransformer(BaseTransformer):
    """
    Randomly occlude a given percentage of sensors on every observation.
    Randomly occludes different ones every time
    """

    def __init__(self, env, percent_of_sensors_to_occlude=.15):
        """
        Knock out random sensors
        """
        self.percent_of_sensors_to_occlude = percent_of_sensors_to_occlude
        self.obs_dims = env.observation_space.flat_dim

    def occlude(self, obs):
        sensor_idx = np.random.randint(0, self.obs_dims-1, size=int(self.obs_dims * self.percent_of_sensors_to_occlude))
        obs[sensor_idx] = 0
        return obs

    def transform(self, observation):
        return self.occlude(observation)
