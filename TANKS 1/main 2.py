from hitbox import Hitbox

hb1 = Hitbox(x=150,y=100,width=100,height=100)#красный
hb2 = Hitbox(x=0,y=100,width=100,height=100)#синий танк
hb3 = Hitbox(x=-150,y=100,width=100,height=100)#зеленый танк





intersection = hb1.intersects(hb2)
intersection2 = hb2.intersects(hb3)
intersection3 = hb1.intersects(hb3)
print(intersection)
print(intersection2)
print(intersection3)