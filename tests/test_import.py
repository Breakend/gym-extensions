import gym_extensions
import gym

# TODO: make these official unit tests and runable with nosetests
def run_test_imports():
    """
    Test import of official envs as seen in the README
    """
    envs = []
    envs.extend([x for x in gym_extensions.continuous.mujoco.custom_envs.keys()])
    envs.extend([x for x in gym_extensions.discrete.classic.custom_envs.keys()])
    envs.extend([x for x in gym_extensions.continuous.box2d.custom_envs.keys()])

    for x in envs:
        print(x)

    for x in envs:
        made = gym.make(x)

    for i in range(10):
        for j in range(3):
            make = gym.make('State-Based-Navigation-2d-Map%d-Goal%d-v0' % (i, j))
            make = gym.make('State-Based-Navigation-2d-Map%d-Goal%d-KnownGoalPosition-v0' % (i, j))
            make = gym.make('Limited-Range-Based-Navigation-2d-Map%d-Goal%d-v0' % (i, j))
            make = gym.make('Limited-Range-Based-Navigation-2d-Map%d-Goal%d-KnownPositions-v0' % (i, j))
            make = gym.make('Image-Based-Navigation-2d-Map%d-Goal%d-v0' % (i, j))

run_test_imports()
