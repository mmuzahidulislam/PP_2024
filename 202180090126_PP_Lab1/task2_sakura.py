import turtle

t = turtle.Turtle()
t.pensize(5)
t.speed(0)
t.color('pink')

radius = 30
angle = 90


def circle_creation():
    for k in range(12):
        t.circle(radius, angle)
        t.left(angle)
        t.circle(radius, angle)
        t.left(angle)
        t.left(radius)
def circle_position():
    for i in range(5):
        for j in range(5):
            t.penup()
            t.goto(-200 + i * 80, -100 + j * 80)
            t.pendown()
            circle_creation()


circle_position()
turtle.done()
t.hideturtle()