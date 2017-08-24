import gym
import os
import gym.envs.mujoco

custom_envs = {
            # Pusher modifications
            "PusherMovingGoal-v0":
                dict(path='gym_extensions.continuous.mujoco.modified_arm:PusherMovingGoalEnv',
                     max_episode_steps=100,
                     reward_threshold=0.0,
                     kwargs= dict()),
            # Pusher modifications
            "PusherLeftSide-v0":
                dict(path='gym_extensions.continuous.mujoco.modified_arm:PusherLeftSide',
                     max_episode_steps=100,
                     reward_threshold=0.0,
                     kwargs= dict()),
            "PusherFullRange-v0":
                dict(path='gym_extensions.continuous.mujoco.modified_arm:PusherFullRange',
                     max_episode_steps=100,
                     reward_threshold=0.0,
                     kwargs= dict()),
            # Striker
            "StrikerMovingStart-v0":
                dict(path='gym_extensions.continuous.mujoco.modified_arm:StrikerMovingStartStateEnv',
                     max_episode_steps=100,
                     reward_threshold=0.0,
                     kwargs= dict()),

            # modified gravity - Hopper
            "AntGravityMars-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_ant:AntGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-3.711)),
            "AntGravityHalf-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_ant:AntGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-4.905)),
            "AntGravityOneAndHalf-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_ant:AntGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-14.715)),

            "HopperGravityHalf-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-4.905)),
            "HopperGravityThreeQuarters-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-7.3575)),
            "HopperGravityOneAndHalf-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-14.715)),
            "HopperGravityOneAndQuarter-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(gravity=-12.2625)),

            "Walker2dGravityHalf-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dGravityEnv',
                     max_episode_steps=1000,
                     kwargs= dict(gravity=-4.905)),
            "Walker2dGravityThreeQuarters-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dGravityEnv',
                     max_episode_steps=1000,
                     kwargs= dict(gravity=-7.3575)),
            "Walker2dGravityOneAndHalf-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dGravityEnv',
                     max_episode_steps=1000,
                     kwargs= dict(gravity=-14.715)),
            "Walker2dGravityOneAndQuarter-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dGravityEnv',
                     max_episode_steps=1000,
                     kwargs= dict(gravity=-12.2625)),

            "HalfCheetahGravityHalf-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(gravity=-4.905)),
            "HalfCheetahGravityThreeQuarters-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(gravity=-7.3575)),
            "HalfCheetahGravityOneAndHalf-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(gravity=-14.715)),
            "HalfCheetahGravityOneAndQuarter-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahGravityEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(gravity=-12.2625)),

            "HumanoidGravityHalf-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidGravityEnv',
                     max_episode_steps=1000,
                     kwargs= dict(gravity=-4.905)),
            "HumanoidGravityThreeQuarters-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidGravityEnv',
                     max_episode_steps=1000,
                     kwargs= dict(gravity=-7.3575)),
            "HumanoidGravityOneAndHalf-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidGravityEnv',
                     max_episode_steps=1000,
                     kwargs= dict(gravity=-14.715)),
            "HumanoidGravityOneAndQuarter-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidGravityEnv',
                     max_episode_steps=1000,
                     kwargs= dict(gravity=-12.2625)),



            ### Environment with walls
            "AntMaze-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_ant:AntMaze',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict()),
            "HopperStairs-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperStairs',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict()),
            "HopperSimpleWall-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperSimpleWallEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict()),

            "HopperWithSensor-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperWithSensorEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/hopper.xml")),
            "Walker2dWall-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dWallEnv',
                     max_episode_steps=1000,
                     kwargs= dict()),
            "Walker2dWithSensor-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dWithSensorEnv',
                     max_episode_steps=1000,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/walker2d.xml")),
            "HalfCheetahWall-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahWallEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict()),
            "HalfCheetahWithSensor-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahWithSensorEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/half_cheetah.xml")),
            "HumanoidWall-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidWallEnv',
                     max_episode_steps=1000,
                     kwargs= dict()),
            "HumanoidWithSensor-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidWithSensorEnv',
                     max_episode_steps=1000,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/humanoid.xml")),
            "HumanoidStandupWithSensor-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidStandupWithSensorEnv',
                     max_episode_steps=1000,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/humanoidstandup.xml")),
            "HumanoidStandupAndRunWall-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidStandupAndRunWallEnv',
                     max_episode_steps=1000,
                     kwargs= dict()),
            "HumanoidStandupAndRunWithSensor-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidStandupAndRunEnvWithSensor',
                     max_episode_steps=1000,
                     kwargs= dict(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/humanoidstandup.xml")),
            "HumanoidStandupAndRun-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidStandupAndRunEnv',
                     max_episode_steps=1000,
                     kwargs= dict()),

            # Modified body parts - Hopper
            "HopperBigTorso-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(body_parts=["torso_geom"], size_scale=1.25)),
            "HopperBigThigh-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(body_parts=["thigh_geom"], size_scale=1.25)),
            "HopperBigLeg-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(body_parts=["leg_geom"], size_scale=1.25)),
            "HopperBigFoot-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(body_parts=["foot_geom"], size_scale=1.25)),
            "HopperSmallTorso-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(body_parts=["torso_geom"], size_scale=.75)),
            "HopperSmallThigh-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(body_parts=["thigh_geom"], size_scale=.75)),
            "HopperSmallLeg-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(body_parts=["leg_geom"], size_scale=.75)),
            "HopperSmallFoot-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_hopper:HopperModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=3800.0,
                     kwargs= dict(body_parts=["foot_geom"], size_scale=.75)),

            # Modified body parts - Walker
            "Walker2dBigTorso-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["torso_geom"], size_scale=1.25)),
            "Walker2dBigThigh-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["thigh_geom", "thigh_left_geom"], size_scale=1.25)),
            "Walker2dBigLeg-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["leg_geom", "leg_left_geom"], size_scale=1.25)),
            "Walker2dBigFoot-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["foot_geom", "foot_left_geom"], size_scale=1.25)),
            "Walker2dSmallTorso-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["torso_geom"], size_scale=.75)),
            "Walker2dSmallThigh-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["thigh_geom", "thigh_left_geom"], size_scale=.75)),
            "Walker2dSmallLeg-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["leg_geom", "leg_left_geom"], size_scale=.75)),
            "Walker2dSmallFoot-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_walker2d:Walker2dModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["foot_geom", "foot_left_geom"], size_scale=.75)),

            # Modified body parts - HalfCheetah
            "HalfCheetahBigTorso-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(body_parts=["torso"], size_scale=1.25)),
            "HalfCheetahBigThigh-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(body_parts=["fthigh", "bthigh"], size_scale=1.25)),
            "HalfCheetahBigLeg-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(body_parts=["fshin", "bshin"], size_scale=1.25)),
            "HalfCheetahBigFoot-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(body_parts=["ffoot", "bfoot"], size_scale=1.25)),
            "HalfCheetahSmallTorso-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(body_parts=["torso"], size_scale=.75)),
            "HalfCheetahSmallThigh-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(body_parts=["fthigh", "bthigh"], size_scale=.75)),
            "HalfCheetahSmallLeg-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(body_parts=["fshin", "bshin"], size_scale=.75)),
            "HalfCheetahSmallFoot-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(body_parts=["ffoot", "bfoot"], size_scale=.75)),
            "HalfCheetahSmallHead-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(body_parts=["head"], size_scale=.75)),
            "HalfCheetahBigHead-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_half_cheetah:HalfCheetahModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     reward_threshold=4800.0,
                     kwargs= dict(body_parts=["head"], size_scale=1.25)),


            # Modified body parts - Humanoid
            "HumanoidBigTorso-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["torso1", "uwaist", "lwaist"], size_scale=1.25)),
            "HumanoidBigThigh-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["right_thigh1", "left_thigh1", "butt"], size_scale=1.25)),
            "HumanoidBigLeg-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["right_shin1", "left_shin1"], size_scale=1.25)),
            "HumanoidBigFoot-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["left_foot", "right_foot"], size_scale=1.25)),
            "HumanoidSmallTorso-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["torso1", "uwaist", "lwaist"], size_scale=.75)),
            "HumanoidSmallThigh-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["right_thigh1", "left_thigh1", "butt"], size_scale=.75)),
            "HumanoidSmallLeg-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["right_shin1", "left_shin1"], size_scale=.75)),
            "HumanoidSmallFoot-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["left_foot", "right_foot"], size_scale=.75)),
            "HumanoidSmallHead-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["head"], size_scale=.75)),
            "HumanoidBigHead-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["head"], size_scale=1.25)),
            "HumanoidSmallArm-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["right_uarm1", "right_larm", "left_uarm1", "left_larm"], size_scale=.75)),
            "HumanoidBigArm-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["right_uarm1", "right_larm", "left_uarm1", "left_larm"], size_scale=1.25)),
            "HumanoidSmallHand-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["left_hand", "right_hand"], size_scale=.75)),
            "HumanoidBigHand-v0" :
                dict(path='gym_extensions.continuous.mujoco.modified_humanoid:HumanoidModifiedBodyPartSizeEnv',
                     max_episode_steps=1000,
                     kwargs= dict(body_parts=["left_hand", "right_hand"], size_scale=1.25)),
                     }

def register_custom_envs():
    for key, value in custom_envs.items():
        arg_dict = dict(id=key,
                        entry_point=value["path"],
                        max_episode_steps=value["max_episode_steps"],
                        kwargs=value["kwargs"])

        if "reward_threshold" in value:
            arg_dict["reward_threshold"] = value["reward_threshold"]

        gym.envs.register(**arg_dict)

register_custom_envs()
