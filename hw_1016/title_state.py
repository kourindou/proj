from pico2d import *
import game_framework
import boys_state


def handle_events():
    events=get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type==SDL_KEYDOWN:
            if e.key==SDLK_ESCAPE:
                game_framework.quit()
            elif e.key==SDLK_SPACE:
                game_framework.push_state(boys_state)

def enter():
    global image
    image=load_image("title.png")

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
    close_canvas()

def resume():
    pass
