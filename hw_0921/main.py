from pico2d import *
import random

def handle_events():

    global running
    global x, y
    global c_x, c_y


    events=get_events()

    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type == SDL_MOUSEMOTION:
            c_x, c_y=event.x, 590-event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
        self.x=random.randint(0,700)
        self.y=random.randint(90,700)
        self.speed=random.randint(1,5)
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        if(self.x<c_x):
            self.x+=self.speed
        elif(self.x>c_x):
            self.x-=self.speed
        if(self.y<c_y):
            self.y+=self.speed
        elif(self.y>c_y):
            self.y-=self.speed
		

        


open_canvas()     
running=True
c_x=0
c_y=0
g = Grass()
boys = [ Boy() for i in range(20)]

while (running):
    handle_events()
    clear_canvas()
    
    g.draw()
    for b in boys:
        b.draw()
    for b in boys:
        b.update()
    
    update_canvas()
    delay(0.01)
    
close_canvas()
