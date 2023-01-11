from ursina import *    #pip install ursina
from random import randint as r              
adjust=4
min=.5
def update():
    global speedX, speedY, speedZ,min,adjust
    def format(x):return abs(x)%360
    if not False in [False for x in [speedX,speedY,speedZ] if x==0]:
        cube.rotation_x += speedX
        cube.rotation_y += speedY
        cube.rotation_z += speedZ
        cube.rotation_x = format(cube.rotation_x)
        cube.rotation_y = format(cube.rotation_y)
        cube.rotation_z = format(cube.rotation_z)
    else:
        cube.rotation_x+=((round(cube.rotation_x/90)*90)-cube.rotation_x)/adjust
        cube.rotation_y+=((round(cube.rotation_y/90)*90)-cube.rotation_y)/adjust
        cube.rotation_z+=((round(cube.rotation_z/90)*90)-cube.rotation_z)/adjust
    
    speedX*=.98 if not speedX<=min else 0
    speedY*=.98 if not speedY<=min else 0
    speedZ*=.98 if not speedZ<=min else 0
    if held_keys['space']:                  
        speedX=r(5,15)
        speedY=r(5,15)
        speedZ=r(5,15)    

app = Ursina()
cube = Entity(model='cube', color=color.orange, scale=(2,2,2), texture="base")
speedX=0
speedY=0
speedZ=0
app.run()
