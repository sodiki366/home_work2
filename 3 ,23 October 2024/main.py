from Tank import Tank
from tkinter import*
import world
import tank_collection
import texture


KEY_LEFT = 37
KEY_RIGHT = 39
KEY_UP = 38
KEY_DOWN = 40
KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68


FPS = 90
def update():

    tank_collection.update()
    player = tank_collection.get_player()
    w.after(1000//FPS, update)
    world.set_camera_xy(player.get_x()-world.SCREEN_WIDTH//2 + player.get_sise()//2,
                        player.get_y()- world.SCREEN_HEIGHT//2 + player.get_sise()//2)

def check_collision():
    player.inersects(enemy)
    enemy.inersects(player)


def key_press(event):
    player = tank_collection.get_player()
    if event.keycode == KEY_W:
        player.forvard()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()

    elif event.keycode == KEY_UP:
        world.move_camera(0,-5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(0,5)
    elif event.keycode == KEY_LEFT:
        world.move_camera(-5,0)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(5,0)

    elif event.keycode == 32:#32 - пробел
        tank_collection.spawn_enemy()

def load_textures():
    texture.load('tank_up','../img/tank_up.png')
    texture.load('tank_down', '../img/tank_down.png')
    texture.load('tank_left', '../img/tank_left.png')
    texture.load('tank_right', '../img/tank_right.png')

    texture.load(world.BRICK , '../img/brick.png')
    texture.load(world.WATER, '../img/water.png')
    texture.load(world.CONCRETE, '../img/wall.png')
    print(texture._frames)


w = Tk()
load_textures()
w.title('Танки на минималках 2.0')
# 2 ширина и высота определяются через модуль world
canv = Canvas(w, width = world.SCREEN_WIDTH, height = world.SCREEN_HEIGHT, bg = 'alice blue')
canv.pack()


world.initialize(canv)



tank_collection.initialize(canv)


w.bind('<KeyPress>', key_press)



update()
w.mainloop()
