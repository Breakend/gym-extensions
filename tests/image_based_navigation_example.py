import gym
import gym_navigation_2d

from env_generator import EnvironmentGenerator, Environment, EnvironmentCollection, Obstacle
import numpy as np
import time
import cv2

env = gym.make('Image-Based-Navigation-2d-Map0-v0')

# worlds_pickle_filename = './worlds_640x480.pkl'
# worlds = EnvironmentCollection()
# worlds.read(worlds_pickle_filename)
#
# env.world = worlds.map_collection[0]
# env.set_destination(np.array([520.0, 400.0]))
# env.set_initial_position(np.array([200.0, 200.0]))
# env.max_observation_range = 100.0
# env.destination_tolerance_range = 20.0

observation = env.reset()
for t in range(100):
    print 'time', t
    env.render()

    action = env.action_space.sample()

    observation, reward, done, info = env.step(action)

    #obs_bgr = cv2.cvtColor(observation, cv2.COLOR_RGB2BGR)
    #cv2.imshow('frame', obs_bgr)
    #cv2.waitKey(10)

    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
