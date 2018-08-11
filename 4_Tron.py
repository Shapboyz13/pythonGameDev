from turtle import *
from base import square, vector

p1xy = vector(-100, 0)
p1Aim = vector(4, 0)
p1Body = set()

p2xy = vector(100, 0)
p2Aim = vector(-4, 0)
p2Body = set()


def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190


def draw():
    p1xy.move(p1Aim)
    p1Head = p1xy.copy()

    p2xy.move(p2Aim)
    p2Head = p2xy.copy()

    if not inside(p1Head) or p1Head in p2Body:
        print("Player blue won")
        return

    if not inside(p2Head) or p2Head in p1Body:
        print("Player red won")
        return

    p1Body.add(p1Head)
    p2Body.add(p2Head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 50)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1Aim.rotate(90), 'w')
onkey(lambda: p1Aim.rotate(-90), 's')
onkey(lambda: p2Aim.rotate(-90), 'Up')
onkey(lambda: p2Aim.rotate(90), 'Down')
draw()
done()
