import missile_collection
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
def update ():
    tank_collection.update()
    missile_collection.update()
    player = tank_collection.get_player()
    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_size() // 2,
                        player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_size() // 2)
    world.update_map()
    w.after(1000//FPS, update)






def key_press(event):

    player = tank_collection.get_player()
    if player.is_destroyed():
        return

    elif event.keycode == KEY_W:
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
        player.fire()

def load_textures():
    texture.load('tank_up','../img/tank_up.png')
    texture.load('tank_down', '../img/tank_down.png')
    texture.load('tank_left', '../img/tank_left.png')
    texture.load('tank_right', '../img/tank_right.png')

    texture.load('tank_up_player', '../img/tank_up_player.png')
    texture.load('tank_down_player', '../img/tank_down_player.png')
    texture.load('tank_left_player', '../img/tank_left_player.png')
    texture.load('tank_right_player', '../img/tank_right_player.png')

    texture.load(world.BRICK , '../img/brick.png')
    texture.load(world.WATER, '../img/water.png')
    texture.load(world.CONCRETE, '../img/wall.png')
    texture.load(world.MISSLE,'../img/bonus.png')
    print(texture._frames)

    texture.load('missile_up', '../img/missile_up.png')
    texture.load('missile_down', '../img/missile_down.png')
    texture.load('missile_left', '../img/missile_left.png')
    texture.load('missile_right', '../img/missile_right.png')



w = Tk()
load_textures()
w.title('Танки на минималках 2.0')
# 2 ширина и высота определяются через модуль world
canv = Canvas(w, width = world.SCREEN_WIDTH, height = world.SCREEN_HEIGHT, bg = '#8ccb5e')
canv.pack()
world.initialize(canv)
tank_collection.initialize(canv)
missile_collection.initialize(canv)
w.bind('<KeyPress>', key_press)
update()
w.mainloop()
