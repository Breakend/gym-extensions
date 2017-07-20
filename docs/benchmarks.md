# Benchmarks!

Part of our goal in releasing these environments is so people can upload their algorithm benchmark results. In the spirit of doing so, we start off with some simple TRPO results. First, we define several task groupings which may be of use to run together. Then we provide some results from running TRPO sequentially across these groupings. While these aren't the only set of combinations, task groupings, and experiments that can be done with these environments, we show that our results show some fundamental problems with lifelong learning or multitask learning (such as catastrophic forgetting, information generalization, etc.).

## Possible Task Groupings

## Benchmark Results

+ [TRPO](benchmark_algos/trpo)

## Uploading Algorithm Results

To upload your algorithms' results, please send a pull request with a doc page as in the *docs/benchmark_algos/trpo* folder.

We require three sections:

1. Algorithm description and link to code (also include hyperparameters used)
2. Task Groupings and Experimental Setup (number of trials, sequential vs. simultaneous learning, etc.)
3. Results (Average Reward, Std. Deviation of reward, number of trials, etc. on each environment in the grouping)
