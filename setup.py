from setuptools import setup
import sys
from os.path import abspath, join, dirname, realpath

def read_requirements_file(filename):
    req_file_path = '%s/%s' % (dirname(realpath(__file__)), filename)
    with open(req_file_path) as f:
        return [line.strip() for line in f]

# only support 2.7 for mujoco compatibility
if sys.version_info < (2,7):
    print('Sorry, Python < 2.7 is not supported, please install Python 3.5.2')
    sys.exit()

setup(name='gym_extensions',
      version='0.0.1',
      packages=['gym_extensions'],
      python_requires='>=3.5',
      install_requires=read_requirements_file('requirements.txt'),
      # mujoco just released 1.5, for now stick with 1.3
      #extras_requires={'mujoco':'mujoco-py<1.50.2,>=1.50.1'},
      extras_requires={'mujoco':'mujoco-py<1.50,>=0.5'},
      description='Extensions to OpenAI Gym for multitask learning, inverse reinforcement learning, and other peripheral tasks.',
      #author='Peter Henderson',
      url='https://github.com/Breakend/gym-extensions',
)
