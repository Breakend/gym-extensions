import tensorflow as tf
import time
import rllab.misc.logger as logger
import pickle
from rllab.misc import tensor_utils
import numpy as np
from tqdm import tqdm
import copy

TINY = 1.0e-8

def initialize_uninitialized(sess):
    global_vars          = tf.global_variables()
    is_not_initialized   = sess.run([tf.is_variable_initialized(var) for var in global_vars])
    not_initialized_vars = [v for (v, f) in zip(global_vars, is_not_initialized) if not f]

    print([str(i.name) for i in not_initialized_vars]) # only for testing
    if len(not_initialized_vars):
        sess.run(tf.variables_initializer(not_initialized_vars))

def custom_train(algo, sess=None):
    """
    This is necessary so that we don't wipe away already initialized policy params.
    Ideally, we should pull request this in as an option to RLlab and remove it from here once done
    """
    created_session = True if (sess is None) else False
    if sess is None:
        sess = tf.Session()
        sess.__enter__()

    rollout_cache = []
    initialize_uninitialized(sess)
    algo.start_worker()
    start_time = time.time()
    for itr in range(algo.start_itr, algo.n_itr):
        itr_start_time = time.time()
        with logger.prefix('itr #%d | ' % itr):
            logger.log("Obtaining samples...")
            paths = algo.obtain_samples(itr)
            logger.log("Processing samples...")
            samples_data = algo.process_samples(itr, paths)
            logger.log("Logging diagnostics...")
            algo.log_diagnostics(paths)
            logger.log("Optimizing policy...")
            algo.optimize_policy(itr, samples_data)
            logger.log("Saving snapshot...")
            params = algo.get_itr_snapshot(itr, samples_data)  # , **kwargs)
            if algo.store_paths:
                params["paths"] = samples_data["paths"]
            logger.save_itr_params(itr, params)
            logger.log("Saved")
            logger.record_tabular('Time', time.time() - start_time)
            logger.record_tabular('ItrTime', time.time() - itr_start_time)
            logger.dump_tabular(with_prefix=False)

    algo.shutdown_worker()
    if created_session:
        sess.close()


def rollout_policy(agent, env, max_path_length=200, speedup=1, get_image_observations=False, animated=False):
    """
    Mostly taken from https://github.com/bstadie/third_person_im/blob/master/sandbox/bradly/third_person/algos/cyberpunk_trainer.py#L164
    Generate a rollout for a given policy
    """
    observations = []
    im_observations = []
    actions = []
    rewards = []
    agent_infos = []
    env_infos = []
    o = env.reset()
    path_length = 0

    while path_length <= max_path_length:
        a, agent_info = agent.get_action(o)
        next_o, r, d, env_info = env.step(a)
        observations.append(env.observation_space.flatten(o))

        actions.append(env.action_space.flatten(a))
        agent_infos.append(agent_info)
        env_infos.append(env_info)
        path_length += 1
        o = next_o
        if get_image_observations:
            if not animated:
                pixel_array = env.render(mode="rgb_array")
            else:
                pixel_array = env.render()

            if pixel_array is None and not animated:
                # Not convinced that behaviour works for all environments, so until
                # such a time as I'm convinced of this, drop into a debug shell
                print("Problem! Couldn't get pixels! Dropping into debug shell.")
                import pdb; pdb.set_trace()
            im_observations.append(pixel_array)
        if d:
            rewards.append(r)
            break
        else:
            rewards.append(r)

    if animated:
        env.render(close=True)

    im_observations = tensor_utils.stack_tensor_list(im_observations)
    observations = tensor_utils.stack_tensor_list(observations)
    rewards = tensor_utils.stack_tensor_list(rewards)

    return dict(
        observations=observations,
        im_observations=im_observations,
        actions=tensor_utils.stack_tensor_list(actions),
        rewards=rewards,
        agent_infos=tensor_utils.stack_tensor_dict_list(agent_infos),
        env_infos=tensor_utils.stack_tensor_dict_list(env_infos),
    )
