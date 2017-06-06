import gym
import gym_navigation_2d

from env_generator import EnvironmentGenerator, Environment, EnvironmentCollection, Obstacle
import numpy as np
import time

env = gym.make('State-Based-MDP-Navigation-2d-Map0-v0')

observation = env.reset()
for t in range(100):
    # print('time', t)
    env.render()

    action = env.action_space.sample()

    observation, reward, done, info = env.step(action)

    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
