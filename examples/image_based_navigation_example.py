import gym
from gym_extensions.continuous.gym_navigation_2d.env_generator import Environment, EnvironmentCollection, Obstacle
import numpy as np
import time
import cv2

env = gym.make('Image-Based-Navigation-2d-Map0-Goal0-v0')

observation = env.reset()
for t in range(100):
    env.render()

    action = env.action_space.sample()

    observation, reward, done, info = env.step(np.array([1.,1.]))

    obs_bgr = cv2.cvtColor(observation, cv2.COLOR_RGB2BGR)
    cv2.imshow('frame', obs_bgr)
    cv2.waitKey(10)

    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
