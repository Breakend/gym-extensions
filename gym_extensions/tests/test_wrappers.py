import gym
from gym_extensions.wrappers.observation_transform_wrapper import ObservationTransformWrapper
from gym_extensions.wrappers.transformers import (SimpleNormalizePixelIntensitiesTransformer, 
                                                  ResizeImageTransformer, AppendPrevTimeStepTransformer)
import time

def test_image_resize():
    gymenv = gym.make("Breakout-v4")
    transformers = [SimpleNormalizePixelIntensitiesTransformer(), ResizeImageTransformer(fraction_of_current_size=.35)]
    transformed_env = ObservationTransformWrapper(gymenv, transformers)
    return transformed_env

def test_append_prev_timestep():
    gymenv = gym.make("Hopper-v1")
    transformers = [AppendPrevTimeStepTransformer()]
    transformed_env = ObservationTransformWrapper(gymenv, transformers)
    return transformed_env

for env in [test_image_resize(), test_append_prev_timestep()]:
    env.reset()
    print(env.observation_space)
    for t in range(100):
        env.render()

        start = time.time()
        action = env.action_space.sample()
        end = time.time()


        start = time.time()
        observation, reward, done, info = env.step(action)
        print(observation)
        print(observation.shape)
        end = time.time()

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
