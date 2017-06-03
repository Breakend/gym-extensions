import gym

custom_envs = {
            "CustomHopperGravityHalf-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:ModifiedHopperEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(xml_name='hopper_gravity_half.xml')),
            "CustomHopperGravityThreeQuarters-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:ModifiedHopperEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(xml_name='hopper_gravity_three_quarters.xml')),
            "CustomHopperGravityOneAndHalf-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:ModifiedHopperEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(xml_name='hopper_gravity_one_and_half.xml')),
            "CustomHopperGravityOneAndQuarter-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:ModifiedHopperEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(xml_name='hopper_gravity_one_and_quarter.xml')),
            "HopperWall-v0" :
                dict(path='gym_extensions.continuous.modified_hopper:ModifiedHopperEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(xml_name='hopper_wall.xml')),
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
