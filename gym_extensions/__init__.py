from .continuous import gym_navigation_2d
from .continuous import mujoco
from .continuous import box2d
from .discrete import classic
from .wrappers import transformers,observation_transform_wrapper 

from . import wrappers, continuous, discrete

import sys
if sys.version_info < (2,7):
    sys.exit('Sorry, Python < 2.7 is not supported')
