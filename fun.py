import turtle
import colorsys as cs

turtle.tracer(100)
turtle.bgcolor('black')
turtle.pensize(4)

for j in range(60):
    for i in range(10):
        turtle.color(cs.hsv_to_rgb(i/10, 1, 1))
        turtle.goto(0,0)
        turtle.right(180)
        turtle.forward(100-j*2)
        turtle.right(180)
        turtle.circle(340, 60)
turtle.done()