"""Turtle Project - Birthday Balloons."""
 
__author__ = "730717721"
 
from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    balloons: Turtle = Turtle()
    balloon1(balloons, -300, -120)
    balloon1(balloons, 0, 0)
    balloon1(balloons, 400, 0)
    balloon2(balloons, 300, 100)
    balloon2(balloons, -200, 90)
    balloon_tie1(balloons, -315, -135)
    balloon_tie1(balloons, -15, -15)
    balloon_tie1(balloons, 385, -15)
    balloon_tie2(balloons, 285, 85)
    balloon_tie2(balloons, -215, 75)
    balloon_tail(balloons, -300, -138)
    balloon_tail(balloons, 0, -18)
    balloon_tail(balloons, 400, -18)
    balloon_tail(balloons, 300, 82)
    balloon_tail(balloons, -200, 72)
    balloon_star(balloons, 315, 250)
    balloon_star(balloons, -185, 240)
    done()

def balloon1(happy: Turtle, x: float, y: float) -> None:
    """Draw pink balloons."""
    happy.penup()
    happy.goto(x, y)
    happy.pendown()
    happy.color(215, 134, 116)
    happy.speed(50)
    happy.begin_fill()
    happy.circle(100)
    happy.end_fill()


def balloon2(birthday: Turtle, x: float, y: float) -> None:
    """Draw yellow balloons."""
    birthday.penup()
    birthday.goto(x, y)
    birthday.pendown()
    birthday.color(246, 208, 66)
    birthday.speed(50)
    birthday.begin_fill()
    birthday.circle(100)
    birthday.end_fill()


def balloon_tie1(triangle: Turtle, x: float, y: float) -> None:
    """Pink balloon knot."""
    triangle.penup()
    triangle.goto(x, y)
    triangle.pendown()
    triangle.color(215, 134, 116)
    triangle.speed(50)
    triangle.begin_fill()
    i: int = 0
    while (i < 3):
        triangle.forward(30)
        triangle.left(120)
        i += 1
    triangle.end_fill()


def balloon_tie2(triangle: Turtle, x: float, y: float) -> None:
    """Yellow balloon knot."""
    triangle.penup()
    triangle.goto(x, y)
    triangle.pendown()
    triangle.color(246, 208, 66)
    triangle.speed(50)
    triangle.begin_fill()
    i: int = 0
    while (i < 3):
        triangle.forward(30)
        triangle.left(120)
        i += 1
    triangle.end_fill()


def balloon_tail(tail: Turtle, x: float, y: float) -> None:
    """Draw a balloon string."""
    tail.penup()
    tail.goto(x, y)
    tail.pendown()
    tail.pencolor("black")
    tail.pensize(5)
    tail.speed(50)
    tail.setheading(-90)
    tail.forward(50)
    tail.left(45)
    tail.forward(50)
    tail.right(45)
    tail.forward(50)
    tail.right(45)
    tail.forward(75)
    tail.left(45)
    tail.forward(50)
    tail.left(45)
    tail.forward(50)
    tail.right(45)
    tail.forward(100)
    tail.hideturtle()

def balloon_star(star: Turtle, x: float, y: float) -> None:
    """Draw a blue star on the yellow balloons."""
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color(71, 44, 158)
    star.speed(50)
    star.begin_fill()
    i: int = 0
    while (i < 5):
        star.forward(100)
        star.right(144)
        i += 1
    star.end_fill()

if __name__ == "__main__":
    main()