
from vpython import *
import math,time

scene.title="Mini solar SYsytem -contains few planets"
scene.width=900
scene.height=600
scene.background=color.black
scene.autoscale=False

dt=0.01
run_time=30

sun=sphere(pos=vector(0,0,0),radius=1.2,color=color.yellow,emissive=True)
local_light(pos=sun.pos,color=color.white)

r1=3.0
planet1=sphere(pos=vector(r1,0,0),radius=0.35,color=color.cyan,make_trail=True,retain=200)

r2=5.5
planet2=sphere(pos=vector(r2,0,0),radius=0.5,color=color.orange,make_trail=True,retain=200)

rm=0.8
moon=sphere(pos=planet1.pos+vector(rm,0,0),radius=0.12,color=color.white,make_trail=True,retain=100)

omega1=1.0
omega2=0.6
omegam=4.0

theta1=0.0
theta2=0.0
thetam=0.0
start=time.time()

while True:
    rate(100)
    theta1+=omega1*dt
    theta2+=omega2*dt
    thetam+=omegam*dt
    planet1.pos=vector(r1*math.cos(theta1),0,r1*math.sin(theta1))
    planet2.pos=vector(r2*math.cos(theta2),0,r2*math.sin(theta2))
    moon.pos=planet1.pos+vector(rm*math.cos(thetam),0,rm*math.sin(thetam))
    scene.center=sun.pos
    if run_time is not None and (time.time()-start)>run_time:
        break

print("Simulation ended.")
