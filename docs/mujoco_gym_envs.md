## Continuous Mujoco Modified OpenAI Gym Envs

### Modified Gravity

For the running agents, we provide ready environments with various scales of simulated earth-like gravity, ranging from one half to one and a half of the normal gravity level (−4.91 to −12.26 meters per second squared in increments of .25g earth gravity). We propose that a successful multitask learning algorithm will extract the underlying walking action structure and reuse the applicable knowledge without forgetting how to walk in varying gravity conditions.

**HopperGravityHalf-v0**

The standard Mujoco OpenAI gym hopper task, but with half the gravity

**HopperGravityThreeQuarters-v0**

The standard Mujoco OpenAI gym hopper task, but with .75 the gravity

**HopperGravityOneAndQuarter-v0**

The standard Mujoco OpenAI gym hopper task, but with 1.25 the gravity

**HopperGravityOneAndHalf-v0**

The standard Mujoco OpenAI gym hopper task, but with 1.5 the gravity

**Similarly:**

+ Walker2dGravityHalf-v0
+ Walker2dGravityThreeQuarters-v0
+ Walker2dGravityOneAndQuarter-v0
+ Walker2dGravityOneAndHalf-v0
+ HalfCheetahGravityThreeQuarters-v0
+ HalfCheetahGravityOneAndHalf-v0
+ HalfCheetahGravityOneAndQuarter-v0
+ HalfCheetahGravityHalf-v0
+ HumanoidGravityHalf-v0
+ HumanoidGravityThreeQuarters-v0
+ HumanoidGravityOneAndQuarter-v0
+ HumanoidGravityOneAndHalf-v0

### Humanoid Extended Tasks

We provide a humanoid multitask environment which com- bines the rewards for standing up and running in the same environment. The reward scale for this task is rather large, but aligns with the HumanoidStandup-v1 environment from OpenAI Gym. Additionally we provide a version of each environment with a sensor readout. When no wall is used, all sensors read zero. When a wall is used, each returns a distance to the wall as previously described.

**HumanoidStandupAndRun-v0**

This rewards standing up and running. Combines the reward from HumanoidStandup and Humanoid.

### Random Walls and Sensors

Inspired by the wall jumping experiment in (Finn et al., 2016), we build a set of similar environments by extending the OpenAI running tasks to use a multi-beam noise- less range sensor. We emit ray-beams from the torso of the runner for the measurements (with an arc of 90 de- grees, 10 beams, a maximum sensing distance of 10 meters, and readouts normalized to a range of [0, 1]). We provide the usual running tasks with the sensor perception enabled (with no readings since there is no wall), and extra environ- ments with a wall set in the path of the agent at a location drawn from a uniform distribution from 1.8 to 3.8 meters ahead of the agent’s start location.

**Walker2dWithSensor-v0**

Same as the Walker2d env in OpenAI gym, but with empty sensor readouts (10 by default) which would detect a wall if it were there. This is to keep the state space the same for transfer learning to a Wall env

**Walker2dWall-v0**

Ray tracing distance sensors emitted from the torso (10 rays by default in a 90 degree arc). Return distance as normalized number from 0-1 such that it is a percentage of the overall maximum ray detection distance. A wall is randomly placed in the path of the agent.

**Similarly:**

+ HopperWall-v0
+ HalfCheetahWall-v0
+ HumanoidStandupAndRunWall-v0
+ HumanoidWall-v0
+ HopperWithSensor-v0
+ HumanoidStandupAndRunWithSensor-v0
+ Walker2dWithSensor-v0
+ HumanoidWithSensor-v0
+ HalfCheetahWithSensor-v0
+ HumanoidStandupWithSensor-v0

### Arm envs

In the OpenAI Striker and Pusher tasks, a 7 DoF arm tries to hit a ball into a hole or push a peg to a goal position respectively. We extend these tasks to randomly move the goal position for the Pusher task, and randomly move the ball start position for the Striker task. As in the original tasks, we bound the varied goal or start state within some restricted uniform distribution as domain appropriate.

**StrikerMovingStart-v0**

The Striker-v0 env from OpenAI gym, but with a moving starting position as well as goal.

**PusherMovingGoal-v0**

The Pusher-v0 env from OpenAI gym, but with a moving goal position as well as start position.

### Morphological Modifications

For the running agents, we provide environments which vary the morphology of a specific body part of the agent. We define “Big” bodyparts as scaling the mass and width of the limb by 1.25 and “Small” bodyparts as being scaled by 0.75. We also group categories of limbs for environments with multiple appendages (i.e. humanoid torso includes the abdomen; humanoid thigh also includes the hips; all ap- pendages encompass both the left/right or front/back simultaneously such that a modified thigh includes both thighs).

**Envs**:

+ HopperSmallFoot-v0
+ HopperSmallLeg-v0
+ HopperSmallThigh-v0
+ HopperSmallTorso-v0
+ HopperBigFoot-v0
+ HopperBigLeg-v0
+ HopperBigThigh-v0
+ HopperBigTorso-v0
+ Walker2dSmallFoot-v0
+ Walker2dSmallLeg-v0
+ Walker2dSmallThigh-v0
+ Walker2dSmallTorso-v0
+ Walker2dBigFoot-v0
+ Walker2dBigLeg-v0
+ Walker2dBigThigh-v0
+ Walker2dBigTorso-v0
+ HalfCheetahSmallFoot-v0
+ HalfCheetahSmallLeg-v0
+ HalfCheetahSmallThigh-v0
+ HalfCheetahSmallTorso-v0
+ HalfCheetahBigFoot-v0
+ HalfCheetahBigLeg-v0
+ HalfCheetahBigThigh-v0
+ HalfCheetahBigTorso-v0
+ HumanoidSmallFoot-v0
+ HumanoidSmallLeg-v0
+ HumanoidSmallThigh-v0
+ HumanoidSmallTorso-v0
+ HumanoidBigFoot-v0
+ HumanoidBigLeg-v0
+ HumanoidBigThigh-v0
+ HumanoidBigTorso-v0
+ HumanoidSmallHead-v0
+ HumanoidBigHead-v0
+ HumanoidSmallArm-v0
+ HumanoidBigArm-v0
+ HumanoidSmallHand-v0
+ HumanoidBigHand-v0
