"""Turtle Practice."""
from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()

leo.penup()
leo.goto(-150, -120)
leo.pendown()
leo.color(215, 134, 116)

leo.speed(25)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()

bob.penup()
bob.goto(-150, -120)
bob.pendown()
bob.pencolor("black")

bob.speed(50)
bob.hideturtle()

i: int = 0
while (i < 3):
    bob.forward(300)
    bob.left(120)
    i = i + 1


done()