from pico2d import *
import game_framework
import time
import random
import pickle
import title_state


p1y=750
x_speed=0
y_speed=0
shi=7.5
ma=0
pat_c=0
pat2_w=0
pat3_w=1
pat3_speed=4
t_life=0
hp_sta=200

class back:
    def __init__(self):
        global score
        self.q=500
        self.w=-500
        self.image=load_image('res/BG_sky.png')
        self.imagec1=load_image('res/BG_cloud.png')
        self.imagec2=load_image('res/BG_cloud.png')
        self.image_s=load_image('res/BG_s.png')
        self.font=load_font("res/SGALS.ttf",40)
        self.font_n=load_font("res/SGALS.ttf",15)
        score=0
    def draw(self):
        self.image.draw(400,500)
        self.imagec1.draw(400,self.q)
        self.imagec2.draw(400,self.w)
    def draw_s(self):
        self.image_s.draw(700,300)
        self.font.draw(640,300,"TIME",(250,250,250))
        self.font_n.draw(685,250,"%.2f"%score,(250,250,250))
    def update(self):
        global score
        self.q+=5
        self.w+=5
        if self.q>1500:
            self.q=-500
        if self.w>1500:
            self.w=-500
        score=time.time()-start
    
class Enemy:
    def __init__(self):
        global E_B
        self.image=load_image('res/EA.png')
        self.HP=load_image("res/E_HP.png")
        self.HPW=load_image('res/E_HP_W.png')
        self.e_ax=0
        self.hp_sta=200
    def draw(self):
        global hp_sta
        global ex, ey
        self.image.clip_draw(self.e_ax,0,240,120,ex,ey)
        self.HP.draw(hp_sta,580)
        self.HPW.draw(50,580)
    def pat2_set(self):
        global ex
        global pat2_w
        pat2_w=random.randint(1,2)
        if pat2_w==1:
            ex=10
        elif pat2_w==2:
            ex=590
    def pat2_update(self):
        global ex, pat2_w
        if pat2_w==1:
            ex+=9.5
        elif pat2_w==2:
            ex-=9.5


class Player:
    def __init__(self):
        global t_life
        self.image=load_image('res/PA.png')
        self.p_ax=0
        self.life=load_image('res/P_life.png')
        self.life1=load_image('res/P_life.png')
        self.life2=load_image('res/P_life.png')
        t_life=title_state.life
        self.point=load_image('res/p_point.png')
    def draw(self):
        global px, py
        self.image.clip_draw(self.p_ax,0,49,58,px,py)
        self.point.draw(px,py)
        if t_life==3:
            self.life.draw(650,30)
            self.life1.draw(700,30)
            self.life2.draw(750,30)
        if t_life==2:
            self.life.draw(670,30)
            self.life1.draw(730,30)
        if t_life==1:
            self.life.draw(700,30)
        self.p_ax+=49
        if self.p_ax>196:
            self.p_ax=0
    def move(self):
        global x_speed, y_speed
        global px, py
        px=px+x_speed
        py=py+y_speed
        if px>570:
            px=570
        elif px<30:
            px=30
        if py>400:
            py=400
        elif py<0:
            py=0
        

class P_b:
    def __init__(self):
        self.image=load_image('res/P_bullet.png')
        self.x=-20
        self.y=0
        self.P_f=0
        self.sound=load_wav('res/shoot.wav')
        self.sound.set_volume(32)
        if title_state.op==0:
            self.damage=3
        else:
            self.damage=100
    def fire(self):
        global px, py
        self.x=px
        self.y=py+55
        self.P_f=1
        self.sound.play()
    def shoot(self):
        global P_bul
        if self.P_f==1:
            self.image.draw(self.x,self.y)
            self.y+=15
            if self.y>600:
                self.P_f=0
        else:
            if self.x!=-20:
                self.x=-20
                self.y=-20
    def h_check(self):
        global hp_sta
        if self.P_f==1:
            if (self.x<ex+100) and (self.x>ex-100) and (self.y>ey) and (self.y<ey+50):
                hp_sta-=self.damage
                self.P_f=0
        else:
            pass

class E_b:
    image=''
    def __init__(self):
        self.x=-20
        self.y=-20
        self.E_f=1
        self.speed=0
        self.deg=0
        self.p1_x=830
        self.p1_y=-30
        self.p1_xm=10
        self.p1_ym=10
        self.E_p1=0
        if E_b.image=='':
            E_b.image=load_image('res/E_bullet.png')
        self.E_p2=0
        self.E_p3=0
        self.p3_x, self.p3_y=830, 500
        self.p3_xm, self.p3_ym=0, 0
    def normal_f(self):
        global ex, ey
        self.x=ex
        self.y=ey
        self.E_f=1
        self.speed=random.randint(5,17)
        self.deg=random.randint(-100,100)
    def normal_s(self):
        if self.E_f==1:
            E_b.image.draw(self.x,self.y)
            self.x+=self.deg*(0.1)
            self.y-=self.speed
            if (self.y<0) or (self.x>600) or (self.x<0):
                self.E_f=0
        else:
            if self.x != 830:
                self.x=830
                self.y=-20
    def pat1_s(self):
        if self.E_p1==1:
            E_b.image.draw(self.p1_x, self.p1_y)
            self.p1_x+=self.p1_xm
            self.p1_y+=self.p1_ym
            if (self.p1_x>600)or(self.p1_x<0)or(self.p1_y>600)or(self.p1_y<0):
                self.E_p1=0
        else:
            if self.p1_x!=830:
                self.p1_x=830
                self.p1_y=-20
            else:
                pass
    def pat1_f(self):
        global p1y
        self.E_p1=1
        self.p1_ym=0
        self.p1_xm=random.randint(-50,50)*0.1
        while(self.p1_ym==0):
            self.p1_ym=random.randint(-50,50)*0.1
        self.p1_y=p1y
        self.p1_x=300
    def reset(self):
        if self.x!=-20:
            self.x=-20
            self.y=-20
            self.p1_x=400
            self.p1_y=-30
            self.E_p3=0
    def pat3_f(self, speed):
        global pat3_w
        if pat3_w==1:
            self.p3_xm=20
            pat3_w=-1
        elif pat3_w==-1:
            self.p3_xm=-20
            pat3_w=1
        self.p3_ym=random.randint(5,12)
        self.p3_x=300
        self.p3_y=500
        self.E_p3=1
    def pat3_s(self):
        if self.E_p3==1:
            E_b.image.draw(self.p3_x, self.p3_y)
            self.p3_x+=self.p3_xm
            self.p3_y-=self.p3_ym
            if (self.p3_x<0) or (self.p3_x>600):
                self.p3_xm=(-self.p3_xm)
            if self.p3_y<0:
                self.E_p3=0
        else:
            if self.p3_x != 830:
                self.p3_x=830
                self.p3_y=-20
    def nh_check(self):
        global t_life
        if self.E_f==1:
            if (py-5<=self.y-10<py+5) and ((px-5<=self.x-10<px+5) or (px-5<self.x+10<=px+5)):
                self.E_f=0
                t_life-=1
                if t_life<=0:
                    pass
            if (py-5<self.y+10<=py+5) and ((px-5<=self.x-10<px+5) or (px-5<self.x+10<=px+5)):
                self.E_f=0
                t_life-=1
                if t_life<=0:
                    pass
            if (py-5<=self.y-10<py+5) and ((px-5>=self.x-10) and (self.x+10>=px+5)):
                self.E_f=0
                t_life-=1
                if t_life<=0:
                    pass
            if (py-5<self.y+10<=py+5) and ((px-5>self.x-10) and (self.x+10>px+5)):
                self.E_f=0
                t_life-=1
                if t_life<=0:
                    pass
            if (self.y+10>py+5) and (self.y-10<py-5) and (px-5>self.x-10) and (self.x+10>px+5):
                self.E_f=0
                t_life-=1
                if t_life<=0:
                    pass
        else:
            pass
    def p1h_check(self):
        global t_life
        if self.E_p1==1:
            if (py-5<=self.p1_y-10<py+5) and ((px-5<=self.p1_x-10<px+5) or (px-5<self.p1_x+10<=px+5)):
                self.E_p1=0
                t_life-=1
                if t_life<=0:
                    pass
            if (py-5<self.p1_y+10<=py+5) and ((px-5<=self.p1_x-10<px+5) or (px-5<self.p1_x+10<=px+5)):
                self.E_p1=0
                t_life-=1
                if t_life<=0:
                    pass
            if (py-5<=self.p1_y-10<py+5) and ((px-5>=self.p1_x-10) and (self.p1_x+10>=px+5)):
                self.E_p1=0
                t_life-=1
                if t_life<=0:
                    pass
            if (py-5<self.p1_y+10<=py+5) and ((px-5>self.p1_x-10) and (self.p1_x+10>px+5)):
                self.E_p1=0
                t_life-=1
                if t_life<=0:
                    pass
            if (self.p1_y+10>py+5) and (self.p1_y-10<py-5) and (px-5>self.p1_x-10) and (self.p1_x+10>px+5):
                self.E_p1=0
                t_life-=1
                if t_life<=0:
                    pass
        else:
            pass
    def p3h_check(self):
        global t_life
        if self.E_p3==1:
            if (py-5<=self.p3_y-10<py+5) and ((px-5<=self.p3_x-10<px+5) or (px-5<self.p3_x+10<=px+5)):
                self.E_p3=0
                t_life-=1
                if t_life<=0:
                    pass
            if (py-5<self.p3_y+10<=py+5) and ((px-5<=self.p3_x-10<px+5) or (px-5<self.p3_x+10<=px+5)):
                self.E_p3=0
                t_life-=1
                if t_life<=0:
                    pass
            if (py-5<=self.p3_y-10<py+5) and ((px-5>=self.p3_x-10) and (self.p3_x+10>=px+5)):
                self.E_p3=0
                t_life-=1
                if t_life<=0:
                    pass
            if (py-5<self.p3_y+10<=py+5) and ((px-5>self.p3_x-10) and (self.p3_x+10>px+5)):
                self.E_p3=0
                t_life-=1
                if t_life<=0:
                    pass
            if (self.p3_y+10>py+5) and (self.p3_y-10<py-5) and (px-5>self.p3_x-10) and (self.p3_x+10>px+5):
                self.E_p3=0
                t_life-=1
                if t_life<=0:
                    pass
        else:
            pass


class pat:
    def __init__(self):
        self.image1=load_image('res/B_hole.png')
        self.image2=load_image('res/E_LAS.png')
        self.x=30
        self.y=500
        self.ts=time.time()
        self.tp=0
        self.c=1
        self.on=1
        self.pat2_on=1
        self.pat3_st=0
        self.pat3_ti=0
    def check(self):
        global pat_c
        if self.on==1:
            self.tp=time.time()
            if self.tp-self.ts>10:
                pat_c=self.c
                self.on=0
                self.c+=1
                if self.c>3:
                    self.c=1
    def pat1_draw(self):
        self.image1.draw(300,self.y)
    def pat2_draw(self):
        global t_life
        global pat_c
        global ex, pat2_w
        self.image2.draw(ex,70)
        if pat2_w==1:
            if ex>540:
                ex=300
                pat_c=0
                self.on=1
                self.ts=time.time()
        elif pat2_w==2:
            if ex<60:
                ex=300
                pat_c=0
                self.on=1
                self.ts=time.time()
        if (ex-10<px<ex+10):
            ex=300
            pat_c=0
            t_life-=1
            if t_life<=0:
                pass
            self.on=1
            self.ts=time.time()
    def pat1_update(self):
        global pat_c
        global p1y
        global px, py
        self.y-=2
        p1y=self.y
        if px>300:
            px-=5.5
        elif px<300:
            px+=5.5
        if py>self.y:
            py-=5.5
        elif py<self.y:
            py+=5.5
        if self.y<-30:
            self.y=500
            pat_c=0
            self.on=1
            self.ts=time.time()
    def pat3_set(self):
        self.pat3_st=time.time()
    def pat3_che(self):
        global pat_c
        self.pat3_ti=time.time()
        if (self.pat3_ti)-(self.pat3_st)>6:
            pat_c=0
            self.on=1
            self.ts=time.time()

class highscore:
    def __init__(self):
        self.scores=0.00
        self.fonts=load_font("res/SGALS.ttf",30)
    def load(self):
        global Highscore
        with open('res/Highscore.pickle','rb') as f:
            Highscore=pickle.load(f)
        if Highscore<score:
            self.scores=Highscore
            self.fonts.draw(270,100,"Highscore : %.2f"%Highscore,(255,255,255))
        else:
            self.scores=score
            self.fonts.draw(270,100,"Highscore : %.2f"%score,(255,255,255))
    def save(self):
        with open('res/Highscore.pickle','wb') as f:
            pickle.dump(self.scores,f)

class game_end:
    def __init__(self):
        self.ov_bg=load_image('res/GO_screen.png')
        self.cl_bg=load_image('res/GC_screen.png')
        self.ov_wr=load_image('res/GO_wr.png')
        self.cl_wr=load_image('res/GC_wr.png')
        self.font=load_font("res/SGALS.ttf",60)
    def clear_draw(self):
        self.cl_bg.draw(400,300)
        self.cl_wr.draw(400,300)
        self.font.draw(225,200,"score : %.2f"%score,(255,255,255))
        hs.load()
        hs.save()
    def over_draw(self):
        self.ov_bg.draw(400,300)
        self.ov_wr.draw(400,300)
        self.font.draw(70,200,"press space to restart",(255,255,255))
        
        

def enter():
    global Pa, Pb
    global Ea, Eb
    global ex, ey, px, py
    global t, q, w
    global bg
    global start
    global pato
    global che
    global x_speed, y_speed
    global pat_c
    global hp_sta
    global ge
    global hs
    hs=highscore()
    ge=game_end()
    hp_sta=200
    pat_c=0
    x_speed=0
    y_speed=0
    px=300
    py=100
    ex=300
    ey=500
    che=0
    t, q, w= 0, 0, 0
    start=time.time()
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
            if e.key == SDLK_x:
                for i in range(1000):
                    Eb[i].reset()
            if e.key == SDLK_SPACE:
                if t_life<1:
                    enter()
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
    if (t_life>0) and (hp_sta>-302):
        clear_canvas()
        global pat_c
        global pato
        bg.draw()
        if pat_c==0:
            for i in range(1000):
                Eb[i].normal_s()
                Eb[i].nh_check()
        elif pat_c==1:
            pato.pat1_draw()
            for i in range(1000):
                Eb[i].pat1_s()
                Eb[i].p1h_check()
        elif pat_c==2:
            pato.pat2_draw()
        elif pat_c==3:
            for i in range(1000):
                Eb[i].pat3_s()
                Eb[i].p3h_check()
        for i in range(20):
            Pb[i].shoot()
            Pb[i].h_check()
        Ea.draw()
        bg.draw_s()
        Pa.draw()
    elif (t_life<=0) and (hp_sta>-302):
        clear_canvas()
        ge.over_draw()
        update_canvas()
        delay(0.03)
    elif (t_life>0) and (hp_sta<=-302):
        clear_canvas()
        ge.clear_draw()
        update_canvas()
        delay(0.03)
    

def update():
    if (t_life>0) and (hp_sta>-302):
        global t, q, w
        global start
        global pat_c
        global pato
        global che
        global pat3_speed
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
                for i in range(15):
                    Eb[q].normal_f()
                    q+=1
                    if q>=1000:
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
                for i in range(18):
                    Eb[w].pat1_f()
                    w+=1
                    if w>=1000:
                        w=0
                t=0
        elif pat_c==2:
            if che==0:
                Ea.pat2_set()
                che=1
            Ea.pat2_update()
        elif pat_c==3:
            if che==0:
                pato.pat3_set()
                for i in range(1000):
                    Eb[i].reset()
                che=1
            pato.pat3_che()
            t+=1
            if t>5:
                for i in range(2):
                    Eb[q].pat3_f(pat3_speed)
                    q+=1
                    if q>=1000:
                        q=0
                t=0
        Pa.move()
        update_canvas()
        delay(0.03)
    else:
        pass

def exit():
    clear_canvas()
