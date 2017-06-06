import gym
import gym_navigation_2d

from env_generator import EnvironmentGenerator, Environment, EnvironmentCollection, Obstacle
import numpy as np
import time

env = gym.make('Limited-Range-Based-POMDP-Navigation-2d-Map1-v0')
#
# worlds_pickle_filename = './worlds_640x480.pkl'
# worlds = EnvironmentCollection()
# worlds.read(worlds_pickle_filename)
#
# env.world = worlds.map_collection[0]
# env.set_initial_position(np.array([-20.0, -20.0]))
# env.set_destination(np.array([520.0, 400.0]))
# env.max_observation_range = 100.0
# env.destination_tolerance_range = 20.0



observation = env.reset()
for t in range(100):
    # print ('time', t)
    env.render()

    action = env.action_space.sample()

    observation, reward, done, info = env.step(action)

    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
