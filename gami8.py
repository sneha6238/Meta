from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
#sky-----------------------------------------------------------------------------------------------------
sky = Sky()

#lighting --------------------------------------------------------------------------------------------
DirectionalLight(y=2,rotation=(45,-45,0),shadows=True)
AmbientLight(color=color.rgba(100,100,100,0.5))

#ground ----------------------------------------------------------------------------------------------------
ground=Entity(
    model='cube',
    scale=(20,1,20),
    collider='box',
    color=color.green,
    position=(0,-0.5,0)
)
#player--------------------------------------------------------------------------------------------------------- ---
player= FirstPersonController()
player.y=2
player.gravity=0.5
player.cursor.visible=True

#Wall ---------------------------------------------------------------------------------------------------------------
wall=Entity(
    model='cube',
    color=color.gray,
    scale=(4,3,0.5),
    position=(0,1.5,10),
    collider='box'
)
wall_lifted=False
wall_lift_distance=3  ########### distance to interact
#blue boxes: to add points 
# treasure glb to replace blue boxes-------------------------------------------- ---
box_positions=[(2,0.5,5),(-2,0.5,7),(4,0.5,8)]
boxes =[]
boxes_spun=[]
for pos in box_positions:
    b = Entity(
        model='models/boxi.glb',  #  glb model
        color=color.white,        
        scale=0.005,                 
        position=pos,
        collider='box'
    )
    boxes.append(b)
    boxes_spun.append(False)


box_spin_distance = 2  # distance to interact


#red boxes: subtract point------------------------------------- ---
red_box_positions = [(-3,0.5,4), (3,0.5,6), (0,0.5,8)]
red_boxes = []
red_boxes_hit = []
for pos in red_box_positions:
    r = Entity(
        model='models/danger.glb',  # your GLB danger model
        color=color.red,            # optional tint
        scale=1.5,                  # scale down to fit the scene
        position=pos,
        collider='box'
    )
    red_boxes.append(r)
    red_boxes_hit.append(False)


red_box_distance=2  # distance to interact

#ui----------------------------------------------------
interaction_text = Text(
    text='',
    position=(-0.85, 0.4), 
    scale=2,
    color=color.yellow
)

score=0
score_text=Text(
    text=f'Score: -{score}',
    position=(-0.85, 0.35),
    scale=2,
    color=color.lime
)

points_display=Text(
    text='',
    position=(0,0.3),  
    scale=2,
    color=color.gold
)
win_text = Text(
    text='',
    position=(0,0),
    scale=3,
    color=color.orange
)

#  updating function ----------------------------------
def update():
    global wall_lifted, score

   
    interaction_text.text = ''
    points_display.text = ''

    #wall interaction ------------------------------------------------------
    if distance(player.position, wall.position)<wall_lift_distance:
        if score >= 100 and not wall_lifted:
            interaction_text.text='Press E to open the door'
            if held_keys['e']:
                wall.animate_y(wall.y+5,duration=1)
                wall_lifted= True
                win_text.text ='You Won!'
                print("Wall lifted! You won!")
        elif not wall_lifted:
            interaction_text.text = 'Gain 100 points to open the door'

    #blue boxes to add points -------------------------------------------
    for i, b in enumerate(boxes):
        if not boxes_spun[i] and distance(player.position, b.position)<box_spin_distance:
            interaction_text.text='Approach to spin the box'
            b.animate_rotation_y(b.rotation_y + 360, duration=1)
            boxes_spun[i]=True
            score += 100
            score_text.text=f'Score: {score}'
            points_display.text='+100 Points!'
            print(f"Box {i+1} spun! +100 Points")

    #redboxes: subtract points ------------------------------------------------------------------
    for i, r in enumerate(red_boxes):
        if not red_boxes_hit[i] and distance(player.position, r.position) < red_box_distance:
            red_boxes_hit[i]=True
            score-=50
            score_text.text=f'Score: {score}'
            points_display.text='-50 Points!'
            print(f"Red Box {i+1} hit! -50 Points")

#run app -======================================================================================--
app.run()
