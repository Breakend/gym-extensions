
## Discrete Envs

We are adding support for discrete envs that are customizable for simple transfer learning tasks. An example is:

```python
gym_extensions.discrete.classic.cartpole.register_custom_cartpole("CartpoleLongPole-v0", gravity=9.8, masscart=1.0, masspole=0.1, pole_length=1.0, force_mag=10.0)
```

Which you can then make with, gym.make("CartpoleLongPole-v0").

While we want to support these custom envs, the main goal of this project is to come up with a standard set of added tasks which can be used for in the contexts of MultiTask or LifeLong learning, particularly in Continuous domains. To that extent, we come up with the following.
