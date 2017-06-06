from rllab.envs.normalized_env import normalize
from rllab.misc.instrument import stub, run_experiment_lite
from rllab.baselines.linear_feature_baseline import LinearFeatureBaseline
from rllab.envs.gym_env import GymEnv

from sandbox.rocky.tf.envs.base import TfEnv
from sandbox.rocky.tf.policies.gaussian_mlp_policy import GaussianMLPPolicy
from sandbox.rocky.tf.algos.trpo import TRPO
from rllab.misc import ext
from sandbox.rocky.tf.optimizers.conjugate_gradient_optimizer import ConjugateGradientOptimizer
from sandbox.rocky.tf.optimizers.conjugate_gradient_optimizer import FiniteDifferenceHvp
import rllab.misc.logger as logger
import gym_extensions
import pickle
import os.path as osp
import numpy as np
from multitask_benchmarks.utils import *

import tensorflow as tf

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("envs", nargs='+', help="The list of environments to train on in order. Eval rollouts will be run on all environments at the end.")
parser.add_argument("--num_epochs", default=100, type=int, help="Number of epochs to run.")
parser.add_argument("--num_final_rollouts", default=20, type=int, help="Number of rollouts to run on final evaluation of environments.")
parser.add_argument("--batch_size", default=25000, type=int, help="Batch_size per epoch (this is the number of (state, action) samples, not the number of rollouts)")
parser.add_argument("--step_size", default=0.01, type=float, help="Step size for TRPO (i.e. the maximum KL bound)")
parser.add_argument("--reg_coeff", default=1e-5, type=float, help="Regularization coefficient for TRPO")
parser.add_argument("--text_log_file", default="./data/debug.log", help="Where text output will go")
parser.add_argument("--tabular_log_file", default="./data/progress.csv", help="Where tabular output will go")
args = parser.parse_args()

# stub(globals())

# ext.set_seed(1)
logger.add_text_output(args.text_log_file)
logger.add_tabular_output(args.tabular_log_file)
logger.set_log_tabular_only(False)

envs = []

for env_name in args.envs:
    gymenv = GymEnv(env_name, force_reset=True, record_video=False, record_log=False)
    env = TfEnv(normalize(gymenv))
    envs.append((env_name, env))

policy = GaussianMLPPolicy(
name="policy",
env_spec=env.spec,
# The neural network policy should have two hidden layers, each with 32 hidden units.
hidden_sizes=(100, 50, 25),
hidden_nonlinearity=tf.nn.relu,
)

baseline = LinearFeatureBaseline(env_spec=env.spec)


with tf.Session() as sess:
    for env_name, env in envs:

        logger.log("Training Policy on %s" % env_name)

        algo = TRPO(
            env=env,
            policy=policy,
            baseline=baseline,
            batch_size=args.batch_size,
            max_path_length=env.horizon,
            n_itr=args.num_epochs,
            discount=0.99,
            step_size=args.step_size,
            optimizer=ConjugateGradientOptimizer(reg_coeff=args.reg_coeff, hvp_approach=FiniteDifferenceHvp(base_eps=args.reg_coeff))
        )

        custom_train(algo, sess=sess)

        rollouts = algo.obtain_samples(args.num_epochs + 1)

        logger.log("Average reward for training rollouts on (%s): %f +- %f " % (env_name, np.mean([np.sum(p['rewards']) for p in rollouts]),  np.std([np.sum(p['rewards']) for p in rollouts])))

    # Final evaluation on all environments using the learned policy

    total_rollouts = []
    for env_name, env in envs:
        rollouts = []
        for i in range(args.num_final_rollouts):
            rollout = rollout_policy(policy, env, max_path_length=env.horizon, speedup=1, get_image_observations=True, animated=True)
            rollouts.append(rollout)
            total_rollouts.append(rollout)

        logger.log("Average reward for eval rollouts on (%s): %f +- %f " % (env_name, np.mean([np.sum(p['rewards']) for p in rollouts]),  np.std([np.sum(p['rewards']) for p in rollouts])))

    logger.log("Total Average across all rollouts and envs: %f +- %f " % (np.mean([np.sum(p['rewards']) for p in total_rollouts]),  np.std([np.sum(p['rewards']) for p in total_rollouts])))
