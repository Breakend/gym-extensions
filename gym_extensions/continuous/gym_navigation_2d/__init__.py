from gym.envs.registration import register
import numpy as np

idx_to_goal = [np.array([460.0, 370.0])] * 10
idx_to_goal[1] = np.array([490.0, 350.0])
idx_to_goal[2] = np.array([460.0, 350.0])
idx_to_goal[3] = np.array([490.0, 370.0])
idx_to_goal[4] = np.array([400.0, 370.0])
idx_to_goal[5] = np.array([350.0, 320.0])
idx_to_goal[6] = np.array([330.0, 250.0])
idx_to_goal[9] = np.array([570.0, 380.0])
idx_to_goal[8] = np.array([430.0, 380.0])

for i in range(10):
    register(
        id='State-Based-Navigation-2d-Map%d-v0' % i,
        entry_point='gym_extensions.continuous.gym_navigation_2d.envs:StateBasedMDPNavigation2DEnv',
        max_episode_steps=1000,
        kwargs=dict(world_idx=i, destination = idx_to_goal[i])
    )
    register(
        id='State-Based-Navigation-2d-Map%d-KnownGoalPosition-v0' % i,
        entry_point='gym_extensions.continuous.gym_navigation_2d.envs:StateBasedMDPNavigation2DEnv',
        max_episode_steps=1000,
        kwargs=dict(world_idx=i, destination = idx_to_goal[i], add_self_position_to_observation=True, add_goal_position_to_observation=True)
    )
    register(
        id='Limited-Range-Based-Navigation-2d-Map%d-v0' % i,
        entry_point='gym_extensions.continuous.gym_navigation_2d.envs:LimitedRangeBasedPOMDPNavigation2DEnv',
        max_episode_steps=1000,
        kwargs=dict(world_idx=i, destination = idx_to_goal[i])
    )
    register(
        id='Limited-Range-Based-Navigation-2d-Map%d-KnownPositions-v0' % i,
        entry_point='gym_extensions.continuous.gym_navigation_2d.envs:LimitedRangeBasedPOMDPNavigation2DEnv',
        max_episode_steps=1000,
        kwargs=dict(world_idx=i, destination = idx_to_goal[i], add_self_position_to_observation=True, add_goal_position_to_observation=True)
    )
    register(
        id='Image-Based-Navigation-2d-Map%d-v0' % i,
        entry_point='gym_extensions.continuous.gym_navigation_2d.envs:ImageBasedNavigation2DEnv',
        max_episode_steps=1000,
        kwargs=dict(world_idx=i, destination = idx_to_goal[i])
    )
