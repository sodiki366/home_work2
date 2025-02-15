
from units import Tank
from random import randint
import world
from missile_collection import check_missiles_collision
from tkinter import NW
id_screen_text = 0
_tanks = []
_canvas = None

def initialize(canv):
    global _canvas , id_screen_text
    _canvas = canv

   #  player = Tank(canvas=canv, x=world.BLOCK_SIZE*2, y=world.BLOCK_SIZE*4, ammo=100, speed=2, bot=False)
   #  enemy = Tank(canvas=canv, x=world.BLOCK_SIZE*4, y=world.BLOCK_SIZE*6, ammo=100, speed=2, bot=True)
   # # neutral = Tank(canvas=canv, x=300, y=300, ammo=100, speed=0, bot=False)
   #  enemy.set_target(player)
    # _tanks.append(player)
    # _tanks.append(enemy)
    player = spawn(False)
    enemy = spawn(True).set_target(player)
    spawn(True).set_target(get_player())

    id_screen_text = _canvas.create_text(10,10,text=_get_screen_text(),
                                         font=('TkDefaultFont', 20, 'bold'),
                                         fill='white', anchor=NW)

def _get_screen_text():
    if get_player().is_destroyed():
        return 'Потрачено'
    if len(_tanks) == 1:
        return ("ПОБЕДА!ВЫ НАСТОЛЬКО КРУТЫ,"
            "ЧТО ДАЖЕ НЕ ПРЕДСТАВИТЬ НАСКОЛЬКО")
    return f'Врагов: {len(_tanks) - 1}'

def _update_screen_text():
    _canvas.itemconfig(id_screen_text, text=_get_screen_text())


def get_player():
    return _tanks[0]

def update():
    _update_screen_text()
    start = len(_tanks) - 1
    for i in range(start, -1, -1):
        if _tanks[i].is_destroyed() and i !=0:
            del _tanks[i]
        else:
            _tanks[i].update()
            check_collision(_tanks[i])
            check_missiles_collision(_tanks[i])
def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.intersects(other_tank):
            return True
    return False

# def spawn_enemy():
#     pos_x =randint(200,800)
#     pos_y = randint(200, 600)
#
#     t = Tank(canvas=_canvas, x=pos_x, y=pos_y, ammo=100, speed=1, bot=True)
#     if not check_collision(t):
#         t.set_target(get_player())
#         _tanks.append(t)
#         return True
def spawn(is_bot=True):
    cols = world.get_cols()
    rows = world.get_rows()
    while True:
        col = randint(1,cols-1)
        row = randint(1,rows-1)

        if world.get_block(row,col) != world.GROUND:
            continue

        t = Tank(_canvas,row,col,bot=is_bot)
        if not check_collision(t):
            _tanks.append(t)
            return t

