
from Tank import Tank
from random import randint
import world

_tanks = []
_canvas = None

def initialize(canv):
    global _canvas
    _canvas = canv

    player = Tank(canvas=canv, x=100, y=50, ammo=100, speed=1, bot=False)
    enemy = Tank(canvas=canv, x=300, y=300, ammo=100, speed=1, bot=True)
   # neutral = Tank(canvas=canv, x=300, y=300, ammo=100, speed=0, bot=False)
    enemy.set_target(player)

    _tanks.append(player)
    _tanks.append(enemy)
    print(_tanks)

def get_player():
    return _tanks[0]

def update():
    for tank in _tanks:
        tank.update()
        check_collision(tank)
def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.inersects(other_tank):
            return True
    return False

def spawn_enemy():
    pos_x =randint(200,800)
    pos_y = randint(200, 600)

    t = Tank(canvas=_canvas, x=pos_x, y=pos_y, ammo=100, speed=1, bot=True)
    if not check_collision(t):
        t.set_target(get_player())
        _tanks.append(t)
        return True
