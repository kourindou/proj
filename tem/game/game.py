from pico2d import *
import game_framework

px=400
py=200
x_speed=0
y_speed=0
ma=0

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
        global x_speed, y_speed
        global px, py
        px=px+x_speed
        py=py+y_speed
        if px>800:
            px=800
        elif px<0:
            px=0
        if py>1000:
            py=1000
        elif py<0:
            py=0

class P_b:
    def __init__(self):
        self.image=load_image('P_bullet.png')
        self.x=0
        self.y=0
        self.P_f=0
    def fire(self):
        global px, py
        self.x=px
        self.y=py+55
        self.P_f=1
    def shoot(self):
        global P_bul
        if self.P_f==1:
            self.image.draw(self.x,self.y)
            self.y+=15
            if self.y>1000:
                self.P_f=0     

def enter():
    global Pa
    global Pb
    global back
    open_canvas(800,1000)
    back=load_image('BG.png')
    back.draw(400,500)
    Pa=Player()
    Pb=[P_b() for i in range(20)]
    update_canvas()
    
def handle_events():
    global x_speed, y_speed
    global Pb
    global ma
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_RIGHT:
                x_speed+=5
            if e.key == SDLK_LEFT:
                x_speed-=5
            if e.key == SDLK_UP:
                y_speed+=5
            if e.key == SDLK_DOWN:
                y_speed-=5
            if e.key == SDLK_z:
                Pb[ma].fire()
                ma+=1
                if ma>19:
                    ma=0
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_RIGHT:
                x_speed-=5
            if e.key == SDLK_LEFT:
                x_speed+=5
            if e.key == SDLK_UP:
                y_speed-=5
            if e.key == SDLK_DOWN:
                y_speed+=5

def draw():
    clear_canvas()
    global Pa
    global Pb
    global back
    back.draw(400,500)
    for i in range(20):
        Pb[i].shoot()
    Pa.draw()
    

def update():
    global Pa
    Pa.move()
    update_canvas()
    delay(0.03)
    pass

def exit():
    close_canvas()
