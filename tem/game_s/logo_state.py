from pico2d import *
import game_framework
import title_state

x=0

def handle_events():
    pass

def enter():
    global image
    open_canvas()
    image=load_image("../res/kpu_credit.png")

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def pause():
    clear_canvas()

def update():
    global x
    global running
    x+=1
    delay(0.01)
    if(x>=100):
        game_framework.push_state(title_state)

def exit():
    close_canvas()
