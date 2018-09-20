from pico2d import *

def handle_events():

    global running
    global x, y
    global c_x, c_y
    global speed
    global dir


    events=get_events()

    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type == SDL_MOUSEMOTION:
            c_x, c_y=event.x, 590-event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            
running=True
x=0
y=0
c_x=0
c_y=0
frame=0
dir=0
speed=5

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

while (running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8
    update_canvas()
    if(x<c_x):
        x+=speed
    elif(x>c_x):
        x-=speed
    if(y<c_y):
        y+=speed
    elif(y>c_y):
        y-=speed
    handle_events()
    delay(0.01)
    
close_canvas()
