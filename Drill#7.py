from pico2d import *
import random

# Game object class here
class Grass:
    # 생성자 이용해 객체의 초기 상태를 정의
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image("animation_sheet.png")
        self.x, self.y = random.randint(0, 100), 90
        self.frame = random.randint(0, 7)
        self.state = 1 # animation state -> 0 : left_run // 1 : right_run // 2 : left_stand // 3 : right_stand
        self.dir = 0 # move dir -> -1 : left // 0 : neut // 1 : right

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, self.state*100, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        coin = random.randint(0, 1)
        if coin == 0: self.image = load_image("ball41x41.png")
        else: self.image = load_image("ball21x21.png")

        self.x, self.y = random.randint(0, 800), 599
        self.fall_speed = random.randint(10, 30)

    def update(self):
        self.y -= self.fall_speed
        if self.y <= 30: self.y = 30

    def draw(self):
        self.image.draw(self.x, self.y)

# ========== Function ==========

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():# 각종 상호작용
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def reset_world(): # 초기화
    global running
    global grass
    global team
    global world
    global Balls

    running = True
    world = []
    grass = Grass() #Grass 클래스를 이용해 grass 객체 생성
    world.append(grass)

    team = [ Boy() for i in range(11) ]
    world += team

    balls = [ Ball() for i in range(20) ]
    world += balls

def clamp(value, min_value, max_value):
    return max(min(value, max_value))

# ============== main ======================

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
