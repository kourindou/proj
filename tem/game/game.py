from pico2d import *
import game_framework
import time
import random

px=400
py=200
ex=400
ey=800
p1y=750
x_speed=0
y_speed=0
shi=7.5
ma=0
pat_c=0

class back:
    def __init__(self):
        self.q=500
        self.w=-500
        self.image=load_image('BG_sky.png')
        self.imagec1=load_image('BG_cloud.png')
        self.imagec2=load_image('BG_cloud.png')
    def draw(self):
        self.image.draw(400,500)
        self.imagec1.draw(400,self.q)
        self.imagec2.draw(400,self.w)
    def update(self):
        self.q+=5
        self.w+=5
        if self.q>1500:
            self.q=-500
        if self.w>1500:
            self.w=-500
    
class Enemy:
    def __init__(self):
        global E_B
        self.image=load_image('EA.png')
        self.HP=load_image("E_HP.png")
        self.HPW=load_image('E_HP_W.png')
        self.e_ax=0
        self.hp_sta=400
    def draw(self):
        global ex, ey
        self.image.clip_draw(self.e_ax,0,420,220,ex,ey)
        self.HP.draw(self.hp_sta,950)
        self.HPW.draw(50,950)


class Player:
    def __init__(self):
        self.image=load_image('PA.png')
        self.p_ax=0
        self.life=load_image('P_life.png')
        self.life1=load_image('P_life.png')
        self.life2=load_image('P_life.png')
    def draw(self):
        global px, py
        self.image.clip_draw(self.p_ax,0,120,120,px,py)
        self.life.draw(30,980)
        self.life1.draw(60,980)
        self.life2.draw(90,980)
    def move(self):
        global x_speed, y_speed
        global px, py
        px=px+x_speed
        py=py+y_speed
        if px>800:
            px=800
        elif px<0:
            px=0
        if py>520:
            py=520
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

class E_b:
    def __init__(self):
        self.x=-20
        self.y=-20
        self.E_f=1
        self.speed=0
        self.deg=0
        self.p1_x=400
        self.p1_y=-30
        self.p1_xm=10
        self.p1_ym=10
        self.E_p1=0
        self.image=load_image('E_bullet.png')
    def normal_f(self):
        global ex, ey
        self.x=ex
        self.y=ey
        self.E_f=1
        self.speed=random.randint(5,22)
        self.deg=random.randint(-100,100)
    def normal_s(self):
        if self.E_f==1:
            self.image.draw(self.x,self.y)
            self.x+=self.deg*(0.1)
            self.y-=self.speed
            if self.y<-20:
                self.E_b=0
    def pat1_s(self):
        if self.E_p1==1:
            self.image.draw(self.p1_x, self.p1_y)
            self.p1_x+=self.p1_xm
            self.p1_y+=self.p1_ym
            if (self.p1_x>800)or(self.p1_x<0)or(self.p1_y>1000)or(self.p1_y<0):
                self.E_p1=0
    def pat1_f(self):
        global p1y
        self.E_p1=1
        self.p1_ym=0
        self.p1_xm=random.randint(-50,50)*0.1
        while(self.p1_ym==0):
            self.p1_ym=random.randint(-50,50)*0.1
        self.p1_y=p1y
        self.p1_x=400
    def reset(self):
        self.x=-20
        self.y=-20
        self.p1_x=400
        self.p1_y=-30

class pat:
    def __init__(self):
        self.image1=load_image('B_hole.png')
        self.image2=load_image('E_LAS.png')
        self.x=30
        self.y=750
        self.ts=time.time()
        self.tp=0
        self.c=1
        self.on=1
    def check(self):
        global pat_c
        if self.on==1:
            self.tp=time.time()
            if self.tp-self.ts>10:
                pat_c=self.c
                self.on=0
                self.c+=1
                if self.c>1:
                    self.c=1
    def pat1_draw(self):
        self.image1.draw(400,self.y)
    def pat2_draw(self):
        self.image2.draw(self.x,750)
    def pat1_update(self):
        global pat_c
        global p1y
        global px, py
        self.y-=2
        p1y=self.y
        if px>400:
            px-=5.5
        elif px<400:
            px+=5.5
        if py>self.y:
            py-=5.5
        elif py<self.y:
            py+=5.5
        if self.y<-30:
            self.y=750
            pat_c=0
            self.on=1
            self.ts=time.time()
    def pat2_update(self):
        global pat_c
        self.x+=5
        if self.x>700:
            self.x=30
            pat_c=0
        

def enter():
    global Pa
    global Pb
    global Ea
    global Eb
    global t, q, w
    global bg
    global start
    global pato
    global che
    che=0
    t, q, w= 0, 0, 0
    start=time.time()
    open_canvas(800,1000)
    bg=back()
    Pa=Player()
    Ea=Enemy()
    pato=pat()
    Pb=[P_b() for i in range(20)]
    Eb=[E_b() for i in range(1000)]
    update_canvas()
    
def handle_events():
    global x_speed, y_speed
    global Pb
    global ma
    global shi
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_RIGHT:
                x_speed+=shi
            if e.key == SDLK_LEFT:
                x_speed-=shi
            if e.key == SDLK_UP:
                y_speed+=shi
            if e.key == SDLK_DOWN:
                y_speed-=shi
            if e.key == SDLK_z:
                Pb[ma].fire()
                ma+=1
                if ma>19:
                    ma=0
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_RIGHT:
                x_speed-=shi
            if e.key == SDLK_LEFT:
                x_speed+=shi
            if e.key == SDLK_UP:
                y_speed-=shi
            if e.key == SDLK_DOWN:
                y_speed+=shi

def draw():
    clear_canvas()
    global Pa
    global Pb
    global Eb
    global bg
    global pat_c
    global pato
    bg.draw()
    for i in range(20):
        Pb[i].shoot()
    if pat_c==0:
        for i in range(1000):
            Eb[i].normal_s()
    elif pat_c==1:
        pato.pat1_draw()
        for i in range(1000):
            Eb[i].pat1_s()
    Pa.draw()
    Ea.draw()
    

def update():
    global Pa
    global t, q, w
    global Eb
    global bg
    global start
    global pat_c
    global pato
    global che
    gt=time.time()
    bg.update()
    pato.check()
    if pat_c==0:
        if che==1:
            for i in range(1000):
                Eb[i].reset()
            che=0
        t+=1
        if t>20:
            for i in range(25):
                Eb[q].normal_f()
                q+=1
                if q>=200:
                    q=0
            t=0
    elif pat_c==1:
        if che==0:
            for i in range(1000):
                Eb[i].reset()
            che=1
        pato.pat1_update()
        t+=1
        if t>20:
            for i in range(25):
                Eb[w].pat1_f()
                w+=1
                if w>=1000:
                    w=0
            t=0
    Pa.move()
    update_canvas()
    delay(0.03)
    pass

def exit():
    close_canvas()
