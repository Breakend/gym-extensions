<img src="assets/Mcgill.png" width=25% align="right" />


# gym-extensions
This repo is intended as an extension for OpenAI Gym for auxiliary tasks (multitask learning, transfer learning, inverse reinforcement learning, etc.)

## Install

Currently we are working on a pip install process to make this easier, but for now you can simply do

```bash
git clone https://github.com/Breakend/gym-extensions-multitask.git
export PYTHONPATH="${PYTHONPATH}:./gym-extensions-multitask"
python
>>> import gym_extensions
```

## More info

More information will be provided on our doc website: https://breakend.github.io/gym-extensions/

## Contributions

For contributing environments please use the general directory structure we have in place and provide **pull requests**. We're still working on making this extension to OpenAI gym the best possible so things may change. Any changes to existing environments should involve an incremental update to the name of the environment (i.e. Hopper-v0 vs. Hopper-v1). If you are not associated with McGill and contribute significantly, please add your association to:

<pre>docs/index.md</pre>
