<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
          skipTags: ['script', 'noscript', 'style', 'textarea', 'pre']
        }
      });

    MathJax.Hub.Queue(function() {
        var all = MathJax.Hub.getAllJax(), i;
        for(i=0; i < all.length; i += 1) {
            all[i].SourceElement().parentNode.className += ' has-jax';
        }
    });

</script>

<script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

## Continuous Mujoco Modified OpenAI Gym Environments

### Modified Gravity

For the running agents, we provide ready environments with various scales of simulated earth-like gravity, ranging from one half to one and a half of the normal gravity level (−4.91 to −12.26 $$m\cdot s^{-2}$$ in increments of $$.25\cdot g$$ earth gravity). We propose that a successful multitask learning algorithm will extract the underlying walking action structure and reuse the applicable knowledge without forgetting how to walk in varying gravity conditions.

**HopperGravityHalf-v0**

The standard Mujoco OpenAI gym hopper task with gravity scaled by 0.5

**HopperGravityThreeQuarters-v0**

The standard Mujoco OpenAI gym hopper task with gravity scaled by 0.75

**HopperGravityOneAndQuarter-v0**

The standard Mujoco OpenAI gym hopper task with gravity scaled by 1.25

**HopperGravityOneAndHalf-v0**

The standard Mujoco OpenAI gym hopper task with gravity scaled by 1.5

**Similarly:**

+ Walker2dGravityHalf-v0
+ Walker2dGravityThreeQuarters-v0
+ Walker2dGravityOneAndQuarter-v0
+ Walker2dGravityOneAndHalf-v0
+ HalfCheetahGravityHalf-v0
+ HalfCheetahGravityThreeQuarters-v0
+ HalfCheetahGravityOneAndQuarter-v0
+ HalfCheetahGravityOneAndHalf-v0
+ HumanoidGravityHalf-v0
+ HumanoidGravityThreeQuarters-v0
+ HumanoidGravityOneAndQuarter-v0
+ HumanoidGravityOneAndHalf-v0

### Humanoid Extended Tasks

We provide a humanoid multitask environment which combines the rewards for standing up and running in a single environment. The reward scale for this task is rather large, but aligns with the HumanoidStandup-v1 environment from OpenAI Gym. Additionally we provide a version of each environment with a sensor readout. When no wall is used, all sensors read zero. When a wall is used, each returns a distance to the wall as previously described.

**HumanoidStandupAndRun-v0**

This task rewards standing up and running. Combines the reward functions from HumanoidStandup and Humanoid.

### Random Walls and Sensors

Inspired by the wall jumping experiment in (Finn et al., 2016), we build a set of similar environments by extending the OpenAI running tasks to use a multi-beam noiseless range sensor.

Ray-beams are emitted from the torso of the runner to act as sensor readings. We also provide the usual running tasks with no walls and the sensor perception enabled so that an agent can first be trained with the larger observation vector before being run or trained on the environments with a wall set in the path of the agent.

**Walker2dWithSensor-v0**

This task is identical to the Walker2d environment in OpenAI gym, but with empty sensor readouts (10 extra observations by default) which would detect a wall if it were there. This is to keep the agent's state space the same dimensionality for transfer learning to a Wall environment.

**Walker2dWall-v0**

In this task, the agent is equipped with a noiseless ray tracing 10 beam sensor in an arc of 90 degrees and a maximum sensing distance of 10 meters, with readouts normalized to a range of [0, 1] to make it a percentage of the overall maximum ray detection distance. A wall is randomly placed in the path of the agent, at a location drawn from a uniform distribution from 1.8 to 3.8 meters ahead of the agent’s start location.

**Similarly:**

+ HopperWithSensor-v0
+ HopperWall-v0
+ HalfCheetahWithSensor-v0
+ HalfCheetahWall-v0
+ Walker2dWithSensor-v0
+ Walker2dWall-v0
+ HumanoidWithSensor-v0
+ HumanoidWall-v0
+ HumanoidStandupWithSensor-v0
+ HumanoidStandupAndRunWithSensor-v0
+ HumanoidStandupAndRunWall-v0

### Arm Environments

In the OpenAI Striker and Pusher tasks, a 7 DoF arm tries to hit a ball into a hole or push a peg to a goal position respectively. We extend these tasks to randomly move the goal position for the Pusher task, and randomly move the ball start position for the Striker task. As in the original tasks, we bound the varied goal or start state within some restricted uniform distribution as domain appropriate.

**StrikerMovingStart-v0**

The Striker-v0 env from OpenAI gym, but with a moving starting position as well as goal.

**PusherMovingGoal-v0**

The Pusher-v0 env from OpenAI gym, but with a moving goal position as well as start position.

### Morphological Modifications

For the running agents, we provide environments which vary the morphology of a specific body part of the agent. We define “Big” bodyparts as scaling the mass and width of the limb by 1.25 and “Small” bodyparts as being scaled by 0.75. We also group categories of limbs for environments with multiple appendages (i.e. humanoid torso includes the abdomen; humanoid thigh also includes the hips; all appendages encompass both the left/right or front/back simultaneously such that a modified thigh includes both thighs).

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
