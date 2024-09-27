import turtle
import random
pen = turtle.Turtle()

pen.shape("turtle")
pen.pensize(5)
pen.fillcolor("#add8e6")
pen.speed(.5)

bars = 15

# Position of the Graph
pen.penup()
pen.goto(-320,-250)
pen.pendown()
x = 40
y = 2
def graph():
    for _ in range(bars):
        pen.begin_fill()
        pen.lt(90)
        graph_length = random.randrange(60,600)
        pen.fd(graph_length)
        pen.rt(90)
        pen.fd(x)
        pen.rt(90)
        pen.fd(graph_length)
        if _ < bars-1:
            pen.lt(90)
            pen.fd(y)
        else:
            pen.rt(90)
            pen.fd((bars*(x+y))-y)
        pen.end_fill()



graph()

pen.hideturtle()
turtle.done()
