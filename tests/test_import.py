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

run_test_imports()
