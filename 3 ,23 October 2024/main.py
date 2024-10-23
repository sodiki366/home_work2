from Tank import Tank
from tkinter import *

w = Tk()
w.title('Танки на минималках 2.0')
canv = Canvas(w,width = 800,height = 600,bg = 'purple')
canv.pack()
player = Tank(canvas = canv,x = 100,y = 50,ammo = 100,model = 'T-14 Армата',speed = 10)
enemy = Tank(canvas = canv,x = 300,y = 300,ammo = 100,model = 'T-14 Армата',speed = 10)

KEY_W =87
KEY_S =83
KEY_A=65
KEY_D =68

def check_collision(enemy):
    if player.intersects(enemy):
        print('Танки столкнулись')

def key_press(event):
    if event.keycode == KEY_W:
        './img/tank_up.png'
    if event.keycode == KEY_S:
        './img/tank_down.png'
    if event.keycode == KEY_A:
        './img/tank_left.png'

    if event.keycode == KEY_D:
        './img/tank_right.png'

    check_collision(enemy)

w.bind('<KeyPress>',key_press)
w.mainloop()
