import gym_extensions
import gym

# TODO: make these official unit tests and runable with nosetests
def run_test_imports():
    """
    Test import of official envs as seen in the README
    """
    for x in gym_extensions.register_envs.custom_envs.keys():
        print(x)

    for x in gym_extensions.register_envs.custom_envs.keys():
        made = gym.make(x)

    for i in range(10):
        make = gym.make('State-Based-Navigation-2d-Map%d-v0' % i)
        make = gym.make('State-Based-Navigation-2d-Map%d-KnownGoalPosition-v0' % i)
        make = gym.make('Limited-Range-Based-Navigation-2d-Map%d-v0' % i)
        make = gym.make('Limited-Range-Based-Navigation-2d-Map%d-KnownPositions-v0' % i)
        make = gym.make('Image-Based-Navigation-2d-Map%d-v0' % i)

run_test_imports()
