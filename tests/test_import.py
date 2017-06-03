import gym_extensions

# TODO: make these official unit tests and runable with nosetests
def run_test_imports():
    """
    Test import of official envs as seen in the README
    """
    for x in gym_extensions.custom_envs.keys():
        made = gym.make(x)
