# GymExtensions
This repo is intended as an extension for OpenAI Gym for continuous domains. This means Mujoco or Roboschool envs. Pull requests are welcome.

## Discrete Envs

We are adding support for discrete envs that are customizable for simple transfer learning tasks. An example is:

<pre>
gym_extensions.discrete.classic.cartpole.register_custom_cartpole("CartpoleLongPole-v0", gravity=9.8, masscart=1.0, masspole=0.1, pole_length=1.0, force_mag=10.0)
</pre>

Which you can then make with, gym.make("CartpoleLongPole-v0").

While we want to support these custom envs, the main goal is to come up with a standard set of added tasks which can be used for contexts like MultiTask or LifeLong learning, particularly in Continuous domains. To that extent, we come up with the following.

## Continuous Envs

### Pre-defined tasks

**CustomHopperGravityHalf-v0** 

The standard Mujoco OpenAI gym hopper task, but with half the gravity

**CustomHopperGravityThreeQuarters-v0** 

The standard Mujoco OpenAI gym hopper task, but with .75 the gravity

**CustomHopperGravityOneAndHalf-v0** 

The standard Mujoco OpenAI gym hopper task, but with 1.5 the gravity

**CustomHopperGravityOneAndQuarter-v0** 

The standard Mujoco OpenAI gym hopper task, but with 1.25 the gravity

**HopperWall-v0** 

The standard Mujoco OpenAI gym hopper task but with a wall place randomly in the path

