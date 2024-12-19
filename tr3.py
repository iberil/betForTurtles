import turtle
import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
t = Turtle()
acilar= [0,90,180,270]
t.pensize(width=5)
t.speed(0.5)
# screen.tracer(0)
def renk():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

for i in range(25000):
    t.color(renk())
    if t.xcor()>=200 and t.heading()==0:
        t.setx(200)
        t.setheading(180)
    elif t.xcor()<=-200 and t.heading()==180:
        t.setx(-200)
        t.setheading(0)
    elif t.ycor()>=200 and t.heading()==90:
        t.sety(200)
        t.setheading(270)
    elif t.ycor()<=-200 and t.heading()==270:
        t.sety(-200)
        t.setheading(90)
    else:
        t.forward(50)
        t.setheading(random.choice(acilar))


for i in range(10000):
    screen.update()

screen.exitonclick()