<img src="assets/Mcgill.png" width=25% align="right" />


# gym-extensions
This python package is an extension to OpenAI Gym for auxiliary tasks (multitask learning, transfer learning, inverse reinforcement learning, etc.)

## Install

```bash
git clone https://github.com/Breakend/gym-extensions-multitask.git
pip3 install -e .
>>> import gym_extensions
```

### Possible Issues

Due to the dependency on OpenAI gym you may have some trouble when installing gym on macOS, to remedy:

```bash
# as per: https://github.com/openai/gym/issues/164
export MACOSX_DEPLOYMENT_TARGET=10.12; pip install -e .
```

## More info

More information will be provided on our doc website: https://breakend.github.io/gym-extensions/

## Contributions

To contributing environments please use the general directory structure we have in place and provide **pull requests**. We're still working on making this extension to OpenAI gym the best possible so things may change. Any changes to existing environments should involve an incremental update to the name of the environment (i.e. Hopper-v0 vs. Hopper-v1). If you are not associated with McGill and contribute significantly, please add your association to:

<pre>docs/index.md</pre>

## Contributors

Here's a list of contributors!

+ <a href="https://github.com/Breakend">@Breakend</a>
+ <a href="https://github.com/weidi-chang">@weidi-chang</a>
+ <a href="https://github.com/florianshkurti">@florianshkurti</a>
+ <a href="https://github.com/vBarbaros">@vBarbaros</a>
