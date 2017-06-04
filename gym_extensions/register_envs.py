import gym
import os
import gym.envs.mujoco

custom_envs = {
            "HopperGravityHalf-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-4.905)),
            "HopperGravityThreeQuarters-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-7.3575)),
            "HopperGravityOneAndHalf-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-14.715)),
            "HopperGravityOneAndQuarter-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-12.2625)),
            "Walker2dGravityHalf-v0" :
                dict(path='gym_extensions.continuous.modified_walker2d:Walker2dGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-4.905)),
            "Walker2dGravityThreeQuarters-v0" :
                dict(path='gym_extensions.continuous.modified_walker2d:Walker2dGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-7.3575)),
            "Walker2dGravityOneAndHalf-v0" :
                dict(path='gym_extensions.continuous.modified_walker2d:Walker2dGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-14.715)),
            "Walker2dGravityOneAndQuarter-v0" :
                dict(path='gym_extensions.continuous.modified_walker2d:Walker2dGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-12.2625)),
            "HalfCheetahGravityHalf-v0" :
                dict(path='gym_extensions.continuous.modified_half_cheetah:HalfCheetahGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-4.905)),
            "HalfCheetahGravityThreeQuarters-v0" :
                dict(path='gym_extensions.continuous.modified_half_cheetah:HalfCheetahGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-7.3575)),
            "HalfCheetahGravityOneAndHalf-v0" :
                dict(path='gym_extensions.continuous.modified_half_cheetah:HalfCheetahGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-14.715)),
            "HalfCheetahGravityOneAndQuarter-v0" :
                dict(path='gym_extensions.continuous.modified_half_cheetah:HalfCheetahGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-12.2625)),
            "HumanoidGravityHalf-v0" :
                dict(path='gym_extensions.continuous.modified_humanoid:HumanoidGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-4.905)),
            "HumanoidGravityThreeQuarters-v0" :
                dict(path='gym_extensions.continuous.modified_humanoid:HumanoidGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-7.3575)),
            "HumanoidGravityOneAndHalf-v0" :
                dict(path='gym_extensions.continuous.modified_humanoid:HumanoidGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-14.715)),
            "HumanoidGravityOneAndQuarter-v0" :
                dict(path='gym_extensions.continuous.modified_humanoid:HumanoidGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-12.2625)),
            "HopperWall-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperWallEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict()),
            "HopperWithSensor-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:HopperWithSensorEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/hopper.xml")),
            "Walker2dWall-v0" :
                dict(path='gym_extensions.continuous.modified_walker2d:Walker2dWallEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict()),
            "Walker2dWithSensor-v0" :
                dict(path='gym_extensions.continuous.modified_walker2d:Walker2dWithSensorEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/walker2d.xml")),
            "HalfCheetahWall-v0" :
                dict(path='gym_extensions.continuous.modified_half_cheetah:HalfCheetahWallEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict()),
            "HalfCheetahWithSensor-v0" :
                dict(path='gym_extensions.continuous.modified_half_cheetah:HalfCheetahWithSensorEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/half_cheetah.xml")),
            "HumanoidWall-v0" :
                dict(path='gym_extensions.continuous.modified_humanoid:HumanoidWallEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict()),
            "HumanoidWithSensor-v0" :
                dict(path='gym_extensions.continuous.modified_humanoid:HumanoidWithSensorEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/humanoid.xml")),
            "HumanoidStandupAndRunWall-v0" :
                dict(path='gym_extensions.continuous.modified_humanoid:HumanoidStandupAndRunWallEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict()),
            "HumanoidStandupAndRunWithSensor-v0" :
                dict(path='gym_extensions.continuous.modified_humanoid:HumanoidStandupAndRunEnvWithSensor',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/humanoidstandup.xml")),
            "HumanoidStandupAndRun-v0" :
                dict(path='gym_extensions.continuous.modified_humanoid:HumanoidStandupAndRunEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict()),
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
