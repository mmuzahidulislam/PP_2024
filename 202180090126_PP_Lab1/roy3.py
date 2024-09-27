import turtle
import math

screen = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.goto(-350,-20)
t.pendown()
t.pensize(4)
t.speed(8)
t.color("blue","red")

def draw_shape(sides, radius):
    angle = 360 / sides
    side_length = 2 * radius * math.sin(math.pi / sides)
    t.right(angle / 2)
    t.begin_fill()
    for _ in range(sides):
        t.backward(side_length)
        t.right(angle)
    t.end_fill()
    t.left(angle / 2)
    t.forward(120)

def draw_circle(radius):
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_all_shapes():
    shapes = [3,4,5,6,7,8,"circle"]
    radius = 35

    for shape in shapes:
        if shape == 'circle':
            draw_circle(radius)
        else:
            draw_shape(shape, radius)


draw_all_shapes()
t.right(90)
turtle.done()