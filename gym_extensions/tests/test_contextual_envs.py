import gym
from gym.envs.classic_control.cartpole import CartPoleEnv
from gym.envs.classic_control.pendulum import PendulumEnv
from gym_extensions.discrete import classic

def test_cartpole_contextual():
    env_id = 'CartPoleContextual-v0'
    env = gym.make(env_id)
    if isinstance(env.unwrapped, CartPoleEnv):
        env.reset()
    else:
        raise NotImplementedError

    nr_of_items_context_space_info = 10
    nr_unwrapped = len(list(env.unwrapped.context_space_info().keys()))
    if nr_of_items_context_space_info != nr_unwrapped:
        print('context_space_info() function needs to be implemented!')
        raise NotImplementedError

    context_vect = [0.01, 0.01, 0.01, 0.01]
    # these should change because change_context_function
    if context_vect == env.unwrapped.context:
        raise AttributeError

    env.unwrapped.change_context(context_vect)
    if context_vect != env.unwrapped.context:
        raise AttributeError


def test_pendulum_contextual():
    env_id = 'PendulumContextual-v0'
    env = gym.make(env_id)
    if isinstance(env.unwrapped, PendulumEnv):
        env.reset()
    else:
        raise NotImplementedError

    nr_of_items_context_space_info = 10
    nr_unwrapped = len(list(env.unwrapped.context_space_info().keys()))
    if nr_of_items_context_space_info != nr_unwrapped:
        print('context_space_info() function needs to be implemented!')
        raise NotImplementedError

    context_vect = [0.01, 0.01]
    if context_vect == env.unwrapped.context:
        raise AttributeError

    env.unwrapped.change_context(context_vect)
    if context_vect != env.unwrapped.context:
        raise AttributeError


if __name__ == "__main__":
    test_cartpole_contextual()
    test_pendulum_contextual()
