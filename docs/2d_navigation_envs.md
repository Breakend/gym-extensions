## 2D continuous navigation envs

We also provide several novel 2D environments that focus on navigation tasks with continuous action spaces to enable benchmarking of learning tasks requiring an implicit memory. The tasks take place in a given occupancy grid map. We opt to make the layout and shape of the obstacles as the only disambiguating feature for localizing within the map. Aside from that information, the environment does not have any texture mapping or other distinctive features.
We provide three different types of navigation tasks, increasing in level of difficulty:

+ Image-based navigation where the agent has access to the entire map, including its own position within the map and the destination in the map as part of the image data.
+ State-based navigation, where the agent has access to its own position in the map and the distance and bearing to the closest obstacle. A simpler version also contains the destination coordinates.
+ Navigation based only on local range-and-bearing data around the agent using ray-tracing. It has to perform mapping and estimate its own position within the map (i.e. perform SLAM), while at the same time exploring to find the goal location, and learning to avoid obstacles. We also modify this with a simpler version, where the goal and current position are known as well.

We provide a reward of -1 for every timestep, -5 for obstacle collisions, and +10 for reaching the goal (which also ends the task, similarly to the MountainCar-v0 environment in OpenAI Gym). The action space is the bounded velocity to apply in the x and y directions.

**Environments**

+ Learning to navigate and search in 2D environments observing only raytracing distance readouts (Limited-RangeBased-Navigation-2d-Map{0-9}-Goal{0-2}-v0)
+ Learning to navigate and search in 2D environments observing current position, raytracing distance readouts, and known goal position (Limited-Range-Based-Navigation-2dMap{0-9}-Goal{0-2}-KnownPositions-v0)
+ Learning to navigate and search in 2D environments observing only the 2D map image with goal location and current position highlighted in different colors (Image-BasedNavigation-2d-Map{0-9}-Goal{0-2}-v0)
