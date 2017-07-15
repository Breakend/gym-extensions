## Wrappers

Currently we also begin to provide a set of wrappers based on rllab to wrap OpenAI Gym environments, these typically will filter observations, etc.

Currently these require <a href="https://github.com/openai/rllab">rllab</a> as a dependency, but we're working on removing this dependency. Please send a Pull Request if you want it done sooner!

### Current Wrappers

We only provide one wrapper for now:

**ObservationTransformWrapper** - Provided a list of transformers, run all observations through the transformers.

### Current Transformers

**SimpleNormalizePixelIntensitiesTransformer** - Normalizes pixels (divide by 255)

**ResizeImageTransformer** - Resizes an image by a given percentage

**RandomSensorMaskTransformer** - Randomly occludes some given percentage of the observations at every timestep

### Example Usage

```python
gymenv = gym.make("Hopper-v1")
transformers = [SimpleNormalizePixelIntensitiesTransformer(), ResizeImageTransformer(fraction_of_current_size=.35)]
transformed_env = ObservationTransformWrapper(gymenv, transformers)
```
