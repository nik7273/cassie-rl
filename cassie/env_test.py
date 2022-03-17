import numpy as np

from cassie_env import CassieEnv

from mujoco.cassiemujoco import *
from trajectory.trajectory import CassieTrajectory

traj = CassieTrajectory("trajectory/stepdata.bin")

env = CassieEnv("walking")
csim = CassieSim()

u = pd_in_t()

# test actual trajectory

for i in range(len(traj.qpos)):
    qpos = traj.qpos[i]
    qvel = traj.qvel[i]

    csim.set_qpos(qpos)
    csim.set_qvel(qvel)

    y = csim.step_pd(u)    

    print(i, end='\r')


# test trajectory wrap-around

env.render()
env.reset()

u = pd_in_t()
while True:

    pos, vel = env.get_ref_state()

    env.phase += 1
    # #print(env.speed)
    if env.phase >= 28:
        env.phase = 0
        env.counter += 1
        #break
    env.sim.set_qpos(pos)
    env.sim.set_qvel(vel)
    y = env.sim.step_pd(u)
    env.render()