from pico2d import *
import game_framework

px=400
py=200

class Enemy:
    def __init__(self):
        global E_B
        self.image=load_image('EA.png')


class Player:
    def __init__(self):
        self.image=load_image('PA.png')
        self.p_ax=0
        pass
    def draw(self):
        global px, py
        self.image.clip_draw(self.p_ax,0,120,120,px,py)
    def move(self):
        pass

class P_b:
    def __init(self):
        self.image=load_image('P_bullet.png')

def enter():
    global Pa
    open_canvas(800,1000)
    back=load_image('BG.png')
    back.draw(400,500)
    Pa=Player()
    
    update_canvas()
    
def handle_events():
    pass
    global boys
    global span
    global px, py
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()

def draw():
    global Pa
    Pa.draw()

def update():
    update_canvas()
    pass

def exit():
    close_canvas()
