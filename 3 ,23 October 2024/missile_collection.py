from units import Missile


_missiles = []
_canvas = None

def initialize(canv):
    global _canvas
    _canvas = canv

def fire(owner):
    m = Missile(_canvas , owner)
    _missiles.append(m)

def update():
    start = len(_tanks)
    for i in range(start, -1, -1):
        if _tanks[i].is_destroyed() and i !=0:
            del _tanks[i]
        else:
            _tanks[i].update()
            check_collision(_tanks[i])
            check_missiles_collision(_tanks[i])


def check_missiles_collision(tank):
    for missile in _missiles:
        if missile.get_owner() == tank:
            continue
        if missile.intersects(tank):
            missile.destroy()
            tank.damage(25)
            return




