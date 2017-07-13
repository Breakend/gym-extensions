## SpaceX-like Falcon Rocket

This Falcon rocket lander environment encourages landing on an autonomous floating drone ship. It uses part of the LunarLander environment as a base (from <a href="https://github.com/openai/gym">OpenAI Gym</a> ) and adds some elements that make the task more difficult and interesting as follows.

The state-dimensions contains now 13 params, some of which are part of the drone-ship. The difficulty of the task can be managed in many ways (e.g., adding more/less power to rocket's engines, increasing/decreasing drone's force that pushes it around, so that it oscillates from left to right and back with different velocity, etc).

The reward function accounts for the falcon rocket landing on both legs (otherwise it's not quite a landing), for the angle and the velocity of the drone ship (higher speed, more unstable drone ship, higher the reward); the episodes are done once the rocket has landed, or if the rocket goes below the drone ship level. It also penalizes longer episodes, i.e., more time-steps until a successful landing results in lower reward.

You can land the SpaceX Falcon rocket from the keyboard as well.

[![Take a look at it here ](https://github.com/vBarbaros/gym-extensions/raw/master/assets/Falcon.png)](https://www.youtube.com/watch?v=GpHylnSox_Q&feature=youtu.be "Hope you'll like it!")

Check the source code <a href="https://github.com/vBarbaros/gym-extensions/tree/master/gym_extensions/continuous/box2d">here</a>