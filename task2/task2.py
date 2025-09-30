from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina()
Sky()
DirectionalLight(y=2,rotation=(45,-45,0),shadows=True)
AmbientLight(color=color.rgba(100,100,100,0.5))

ground=Entity(model='cube',scale=(20,1,20),collider='box',color=color.green,position=(0,-0.5,0))

player=FirstPersonController()
player.y=1
player.gravity=0.5
player.cursor.visible=True

door=Entity(model='cube',color=color.gray,scale=(2,3,0.5),position=(0,1.5,8),collider='box')
door_opened=False
door_dist=3

magic_box=Entity(model='cube',color=color.azure,scale=1,position=(3,0.5,3),collider='box')
box_touched=False
box_dist=2

hint=Text(text='',position=(-0.85,0.4),scale=2,color=color.yellow)

def update():
    global door_opened,box_touched
    hint.text=''
    if distance(player.position,door.position)<door_dist and not door_opened:
        hint.text='Press E to open the door'
        if held_keys['e']:
            door.animate_y(door.y+5,duration=1)
            door_opened=True
    if distance(player.position,magic_box.position)<box_dist and not box_touched:
        hint.text='You touched the magic box!'
        magic_box.color=color.random_color()
        box_touched=True

app.run()
