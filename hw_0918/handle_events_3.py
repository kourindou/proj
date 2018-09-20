from pico2d import *

def handle_events():

    global running
    global x, y
    global speed
    global dir
    global c_x, c_y
    global s_x=[]
    global s_y=[]
    global i

    events=get_events()

    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button==SDL_BUTTON_LEFT:
            s_x.append(event.x)
            s_y.append(590-event.y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            
running=True
x=0
y=0
frame=0
dir=0
speed=5
c_x=0
c_y=0
i=1

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

while (running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8
    update_canvas()
    if s_x!=[] and i==1:
        c_x=s_x.pop()
        c_y=s_y.pop()
        i=0
    if (i==0):
        if(x<c_x):
            x+=speed
        elif(x>c_x):
            x-=speed
        if(y<c_y):
            y+=speed
        elif(y>c_y):
            y-=speed
        if(x==c_x and y==c_y):
            i=1
    if(s_x[0]==x and s_y[0]==y):
        for i in range (10):
            s_x[p]=s_[p+1]
            s_y[p]=s_[p+1]
            p+=1
        p=0
        i-=1
        s_x[i]=0
        s_y[i]=0
    handle_events()
    delay(0.01)
    
close_canvas()
