import gym
import gym_extensions
from gym.envs.classic_control.cartpole import CartPoleEnv
from gym.envs.classic_control.pendulum import PendulumEnv


def test_cartpole_contextual(env_id):
    env = gym.make(env_id)
    if isinstance(env.unwrapped, CartPoleEnv):
        env.reset()
    else:
    	raise NotImplementedError

    nr_of_items_context_space_info = 10
    if nr_of_items_context_space_info == len(env.unwrapped.context_space_info().keys()):
    	pass
    else:
    	print 'context_space_info() function needs to be implemented!'
        raise NotImplementedError
    
    context_vect = [0.01, 0.01, 0.01, 0.01]

    if context_vect != env.unwrapped.context:
    	pass
    else:
        raise AttributeError 

    env.unwrapped.change_context(context_vect)

    if context_vect == env.unwrapped.context:
    	pass
    else:
    	raise AttributeError


def test_pendulum_contextual(env_id):
    env = gym.make(env_id)
    if isinstance(env.unwrapped, PendulumEnv):
        env.reset()
    else:
    	raise NotImplementedError

    nr_of_items_context_space_info = 10
    if nr_of_items_context_space_info == len(env.unwrapped.context_space_info().keys()):
    	pass
    else:
    	print 'context_space_info() function needs to be implemented!'
        raise NotImplementedError
    
    context_vect = [0.01, 0.01]

    if context_vect != env.unwrapped.context:
    	pass
    else:
        raise AttributeError 

    env.unwrapped.change_context(context_vect)

    if context_vect == env.unwrapped.context:
    	pass
    else:
    	raise AttributeError



if __name__=="__main__":
	env_id_cartpole = 'CartPoleContextual-v0'
	test_cartpole_contextual(env_id_cartpole)

	env_id_pendulum = 'PendulumContextual-v0'
	test_pendulum_contextual(env_id_pendulum)