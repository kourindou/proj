from pico2d import *
import game_framework
import game


def handle_events():
    events=get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type==SDL_KEYDOWN:
            if e.key==SDLK_ESCAPE:
                game_framework.quit()
            elif e.key==SDLK_SPACE:
                game_framework.push_state(game)

def enter():
    global image
    image=load_image("../res/title.png")

def draw():
    clear_canvas()
    image.draw(400,300)
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

