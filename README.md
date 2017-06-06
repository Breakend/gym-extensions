<img src="https://www.google.ca/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwi4ouDFxanUAhWDx4MKHWhfAngQjRwIBw&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFile%3AMcGill_Wordmark.svg&psig=AFQjCNFIbytZDw0-wn-np97-oEoY35EYJw&ust=1496849629646520" width=25% align="right" />


# gym-extensions(-multitask)
This repo is intended as an extension for OpenAI gym for multitask domains, particularly focusing on continuous domains such as MuJoCo tasks.


## Install

Currently we are working on a pip install process to make this easier, but for now you can simply do

```bash
git clone https://github.com/Breakend/gym-extensions-multitask.git
export PYTHONPATH="${PYTHONPATH}:./gym-extensions-multitask"
python
>>> import gym_extensions
```

## Discrete Envs

We are adding support for discrete envs that are customizable for simple transfer learning tasks. An example is:

```python
gym_extensions.discrete.classic.cartpole.register_custom_cartpole("CartpoleLongPole-v0", gravity=9.8, masscart=1.0, masspole=0.1, pole_length=1.0, force_mag=10.0)
```

Which you can then make with, gym.make("CartpoleLongPole-v0").

While we want to support these custom envs, the main goal is to come up with a standard set of added tasks which can be used for contexts like MultiTask or LifeLong learning, particularly in Continuous domains. To that extent, we come up with the following.

## Continuous Envs

### Modified Gravity

**HopperGravityHalf-v0**

The standard Mujoco OpenAI gym hopper task, but with half the gravity

**HopperGravityThreeQuarters-v0**

The standard Mujoco OpenAI gym hopper task, but with .75 the gravity

**HopperGravityOneAndQuarter-v0**

The standard Mujoco OpenAI gym hopper task, but with 1.25 the gravity

**HopperGravityOneAndHalf-v0**

The standard Mujoco OpenAI gym hopper task, but with 1.5 the gravity


**Similarly:**

Walker2dGravityHalf-v0

Walker2dGravityThreeQuarters-v0

Walker2dGravityOneAndQuarter-v0

Walker2dGravityOneAndHalf-v0

HalfCheetahGravityThreeQuarters-v0

HalfCheetahGravityOneAndHalf-v0

HalfCheetahGravityOneAndQuarter-v0

HalfCheetahGravityHalf-v0

HumanoidGravityHalf-v0

HumanoidGravityThreeQuarters-v0

HumanoidGravityOneAndQuarter-v0

HumanoidGravityOneAndHalf-v0

### Humanoid Extended Tasks


**HumanoidStandupAndRun-v0**

This rewards standing up and running. Combines the reward from HumanoidStandup and Humanoid.

### Random Walls and Sensors

**Walker2dWithSensor-v0**

Same as the Walker2d env in OpenAI gym, but with empty sensor readouts (10 by default) which would detect a wall if it were there. This is to keep the state space the same for transfer learning to a Wall env

**Walker2dWall-v0**

Ray tracing distance sensors emitted from the torso (10 rays by default in a 90 degree arc). Return distance as normalized number from 0-1 such that it is a percentage of the overall maximum ray detection distance. A wall is randomly placed in the path of the agent.

**Similarly:**

HopperWall-v0

HalfCheetahWall-v0

HumanoidStandupAndRunWall-v0

HumanoidWall-v0

HopperWithSensor-v0

HumanoidStandupAndRunWithSensor-v0

Walker2dWithSensor-v0

HumanoidWithSensor-v0

HalfCheetahWithSensor-v0

HumanoidStandupWithSensor-v0

### Arm envs

**StrikerMovingStart-v0**

The Striker-v0 env from OpenAI gym, but with a moving starting position as well as goal.

**PusherMovingGoal-v0**

The Pusher-v0 env from OpenAI gym, but with a moving goal position as well as start position.
