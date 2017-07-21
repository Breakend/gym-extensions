import gym

def test_import_mujoco():
    """
    Test import of official envs as seen in the README
    """
    from gym_extensions.continuous import mujoco
    envs = [x for x in mujoco.custom_envs.keys()]
    [gym.make(x) for x in envs]
    return True
   
if __name__ == '__main__':
    print(test_import_mujoco())
