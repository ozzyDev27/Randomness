from ursina import *    #pip install ursina
from random import randint as r              
adjust=4
def update():
    global speed,adjust
    def format(x):return abs(x)%360
    if not False in [False for x in [speed[0],speed[1],speed[2]] if x==0]:
        cube.rotation_x = format(speed[0])
        cube.rotation_y = format(speed[1])
        cube.rotation_z = format(speed[2])
    else:cube.rotation_x+=((round(cube.rotation_x/90)*90)-cube.rotation_x)/adjust;cube.rotation_y+=((round(cube.rotation_y/90)*90)-cube.rotation_y)/adjust;cube.rotation_z+=((round(cube.rotation_z/90)*90)-cube.rotation_z)/adjust
    speed=[0 if i<.5 else i*.98 for i in speed]
    if held_keys['space']:speed=[r(5,15) for i in speed]
cube = Entity(model='cube', color=color.orange, scale=(2,2,2), texture="base")
speed=[0,0,0]
Ursina().run()
