from setuptools import setup

setup(name='gym_extensions',
      version='0.0.1',
      packages=['gym_extensions'],
      install_requires=['numpy>=1.10.4', 'mujoco_py', 'gym[all]>=0.9.2', 'pyrr', 'six', 'pgyame', 'cached_property'],
      description='Extensions to OpenAI Gym for multitask learning, inverse reinforcement learning, and other peripheral tasks.',
      author='Peter Henderson',
      url='https://github.com/Breakend/gym-extensions',
)
