
from rllab.misc.overrides import overrides
from scipy.misc import imresize
from rllab.spaces.box import Box
from cached_property import cached_property
import scipy.misc
import numpy as np
from rllab.misc.overrides import overrides

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
        raise prev_observation_space

class SimpleNormalizePixelIntensitiesTransformer(BaseTransformer):
    """
    Normalizes pixel intensities simply by dividing by 255.
    """
    @overrides
    def transform(self, observation):
        return np.array(observation).astype(np.float32) / 255.0

    @overrides
    def transformed_observation_space(self, wrapped_observation_space):
        return wrapped_observation_space

class ResizeImageTransformer(BaseTransformer):
    """
    Rescale a given image by a percentage
    """

    def __init__(self, fraction_of_current_size):
        self.fraction_of_current_size = fraction_of_current_size

    @overrides
    def transform(self, observation):
        return scipy.misc.imresize(observation, self.fraction_of_current_size)

    @overrides
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

    @overrides
    def transform(self, observation):
        return self.occlude(observation)
