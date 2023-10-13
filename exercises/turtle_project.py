"""Turtle Project - Balloons."""
 
__author__ = "730717721"
 
from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    balloons: Turtle = Turtle()
    balloon1(balloons, -300, -120)
    balloon1(balloons, 0, 0)
    balloon2(balloons, 300, 100)
    balloon2(balloons, -200, 90)
    balloon_tie1(balloons, -315, -140)
    balloon_tie1(balloons, -15, -20)
    balloon_tie2(balloons, 285, 85)
    balloon_tie2(balloons, -215, 75)

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
        i = i + 1
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
        i = i + 1
    triangle.end_fill()


def balloon_tail(tail: Turtle, x: float, y: float) -> None:
    """Balloon string."""


if __name__ == "__main__":
    main()