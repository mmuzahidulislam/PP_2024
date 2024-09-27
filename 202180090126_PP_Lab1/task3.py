import turtle
import math

#set up turtle window
screen=turtle.Screen()
screen.bgcolor("white")


#set up pen
pen=turtle.Turtle()
pen.pensize(5)
pen.speed(8)
pen.color("blue","red")
pen.shape("turtle")
pen.pu()
pen.goto(-320,0)
pen.pd()

pen.begin_fill()

def draw_polygon(sides):
    radius=30
    side_length = 2 * radius * math.sin(math.pi / sides)
    angle = 360 / sides
    pen.rt(angle/2)
    for _ in range(sides):
        pen.bk(side_length)
        pen.rt(angle)
    pen.lt(angle/2)
    pen.fd(90)


for _ in range(3,10,1):
    draw_polygon(_)

pen.circle(30)
pen.end_fill()
pen.hideturtle()

turtle.done()