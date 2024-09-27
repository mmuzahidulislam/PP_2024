import turtle
import random

screen=turtle.Screen()
t=turtle.Turtle()
t.pensize(4)
t.color("black","gray")
t.speed(0)
t.penup()
t.goto(-335,-180)
t.pendown()

#define function for making bar
def make_graph(bar_heights, bar_width):
    count=0
    bar_distance=3
    bar_num=len(bar_heights)
    for x in bar_heights:
        t.begin_fill()
        t.left(90)
        t.forward(x)
        t.right(90)
        t.forward(bar_width)
        t.right(90)
        t.forward(x)
        count+=1
        t.end_fill()
        if count < bar_num:
            t.lt(90)
            t.fd(bar_distance)
        else:
            t.rt(90)
            t.fd((bar_num*(bar_distance+bar_width))-bar_distance)
        t.end_fill()

bar_heights = [random.randint(45, 450) for _ in range(20)]
make_graph(bar_heights,30) #call function

t.hideturtle()
turtle.done()