from Tank import Tank
from tkinter import *



KEY_W =87
KEY_S =83
KEY_A=65
KEY_D =68

FPS=90


def update():
    player.update()
    check_collision(Enemy)
    w.after(1000//FPS, update)

def check_collision(enemy):
    if player.intersects(enemy):
        print('Танки столкнулись')
        player.undo_move()


def key_press(event):
    if event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()

    elif event.keycode == KEY_D:
        player.right()
    check_collision(Enemy)
w = Tk()
w.title('Танки на минималках 2.0')
canv = Canvas(w,width = 800,height = 600,bg = 'purple')
canv.pack()
player = Tank(canvas = canv,x = 100,y = 50,ammo = 100,model = 'T-14 Армата',speed = 1)
Enemy = Tank(canvas = canv,x = 300,y = 300,ammo = 100,model = 'T-14 Армата',speed = 10)

w.bind('<KeyPress>',key_press)
update()
w.mainloop()
