import gym
import os
import gym.envs.mujoco

custom_envs = {
            "CustomHopperGravityHalf-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-4.905)),
            "CustomHopperGravityThreeQuarters-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-7.3575)),
            "CustomHopperGravityOneAndHalf-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-14.715)),
            "CustomHopperGravityOneAndQuarter-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-12.2625)),
            "HopperWall-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperWallEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict()),
            "HopperWithSensor-v1" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperWithSensorEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/hopper.xml"))
                     }

def register_custom_envs():
    for key, value in custom_envs.items():
        print("Registering %s" % key)
        gym.envs.register(
            id=key,
            entry_point=value["path"],
            max_episode_steps=value["max_episode_steps"],
            reward_threshold=value["reward_threshold"],
            kwargs=value["kwargs"]
        )
