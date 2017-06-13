from gym.envs.registration import register
import numpy as np

# (x,y)
idx_to_goal = [ (np.array([230.0, 430.0]), np.array([230.0, 130.0]), np.array([500.0, 430.0]) )] * 10
idx_to_goal[1] = (np.array([130.0, 370.0]), np.array([130.0, 110.0]), np.array([520.0, 250.0]) )
idx_to_goal[2] = (np.array([530.0, 110.0]), np.array([130.0, 310.0]), np.array([460.0, 330.0]) )
idx_to_goal[3] = (np.array([400.0, 50.0]), np.array([180.0, 320.0]), np.array([430.0, 310.0]) )
idx_to_goal[4] = (np.array([180.0, 380.0]), np.array([610.0, 120.0]), np.array([420.0, 330.0]) )
idx_to_goal[5] = (np.array([500.0, 90.0]), np.array([180.0, 390.0]), np.array([380.0, 320.0]) )
idx_to_goal[6] = (np.array([480.0, 150.0]), np.array([440.0, 380.0]), np.array([310.0, 220.0]) )
idx_to_goal[7] = (np.array([500.0, 380.0]), np.array([470.0, 280.0]), np.array([270.0, 280.0]) )
idx_to_goal[8] = (np.array([250.0, 440.0]), np.array([420.0, 200.0]), np.array([150.0, 180.0]) )
idx_to_goal[9] = (np.array([390.0, 110.0]), np.array([520.0, 350.0]), np.array([240.0, 310.0]) )

for i in range(10):
    for j in range(3):
        register(
            id='State-Based-Navigation-2d-Map%d-Goal%d-v0' % (i, j),
            entry_point='gym_extensions.continuous.gym_navigation_2d.envs:StateBasedMDPNavigation2DEnv',
            max_episode_steps=1000,
            kwargs=dict(world_idx=i, destination = idx_to_goal[i][j])
        )
        register(
            id='State-Based-Navigation-2d-Map%d-Goal%d-KnownGoalPosition-v0' % (i, j),
            entry_point='gym_extensions.continuous.gym_navigation_2d.envs:StateBasedMDPNavigation2DEnv',
            max_episode_steps=1000,
            kwargs=dict(world_idx=i, destination = idx_to_goal[i][j], add_self_position_to_observation=True, add_goal_position_to_observation=True)
        )
        register(
            id='Limited-Range-Based-Navigation-2d-Map%d-Goal%d-v0' % (i, j),
            entry_point='gym_extensions.continuous.gym_navigation_2d.envs:LimitedRangeBasedPOMDPNavigation2DEnv',
            max_episode_steps=1000,
            kwargs=dict(world_idx=i, destination = idx_to_goal[i][j])
        )
        register(
            id='Limited-Range-Based-Navigation-2d-Map%d-Goal%d-KnownPositions-v0' % (i, j),
            entry_point='gym_extensions.continuous.gym_navigation_2d.envs:LimitedRangeBasedPOMDPNavigation2DEnv',
            max_episode_steps=1000,
            kwargs=dict(world_idx=i, destination = idx_to_goal[i][j], add_self_position_to_observation=True, add_goal_position_to_observation=True)
        )
        register(
            id='Image-Based-Navigation-2d-Map%d-Goal%d-v0' % (i, j),
            entry_point='gym_extensions.continuous.gym_navigation_2d.envs:ImageBasedNavigation2DEnv',
            max_episode_steps=1000,
            kwargs=dict(world_idx=i, destination = idx_to_goal[i][j])
        )
