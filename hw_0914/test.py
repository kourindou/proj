from pico2d import *

def go_sq(x,y,frame):
    while((x!=380)|(y!=90)):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame= (frame+1) % 8
        if((y==90) & (400<=x<780)):
            x = x+20
        elif((x==780)&(y<570)):
            y=y+20
        elif((y==570) & (0<x)):
            x=x-20
        elif((x==0)&(90<y)):
            y=y-20
        elif ((y==90)&(0<=x<400)):
            x=x+20
        delay(0.05)

def go_cir(x,y,frame):
    a=22
    b=1
    while((x!=378)|(y!=91)):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame= (frame+1) % 8
        if((400<=x<653)&(90<=y<343)):
            x=x+a
            y=y+b
            if(1<a):
                a=a-1
            if(b<22):
                b=b+1
        elif((400<x<=653)&(343<=y<596)):
            x=x-a
            y=y+b
            if(a<22):
                a=a+1
            if(1<b):
                b=b-1
        elif((147<x<=400)&(343<y<=596)):
            x=x-a
            y=y-b
            if(1<a):
                a=a-1
            if(b<22):
                b=b+1
        elif((147<=x<400)&(90<y<=343)):
            x=x+a
            y=y-b
            if(a<22):
                a=a+1
            if(1<b):
                b=b-1
        delay(0.05)




open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

x=400
y=90
frame=0
while(1):
    go_sq(x,y,frame)
    go_cir(x,y,frame)

close_canvas()
