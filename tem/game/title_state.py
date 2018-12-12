from pico2d import *
import game_framework
import game

life=3
op=0
ch=0

def handle_events():
    global life, ch, op
    events=get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type==SDL_KEYDOWN:
            if e.key==SDLK_ESCAPE:
                game_framework.quit()
            elif e.key==SDLK_SPACE:
                game_framework.push_state(game)
            if e.key==SDLK_RIGHT:
                if life>=3:
                    life=1
                else:
                    life+=1
            if e.key==SDLK_LEFT:
                if life<=1:
                    life=3
                else:
                    life-=1
            if e.key==SDLK_s:
                ch+=1
                if ch>15:
                    ch=0
                    op=1
                    print("op on")
                else:
                    op=0

def enter():
    global image
    global font
    global life
    life=3
    font=load_font("res/SGALS.ttf",30)
    image=load_image("res/title.png")


def draw():
    clear_canvas()
    image.draw(400,300)
    font.draw(250,200,"press space to start",(0,0,0))
    font.draw(350,150,"LIFE : ",(0,0,0))
    font.draw(450,150,str(life),(0,0,0))
    update_canvas()

def pause():
    clear_canvas()
    pass

def update():
    pass

def exit():
    pass

def resume():
    enter()

