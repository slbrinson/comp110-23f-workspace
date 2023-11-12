"""CQ07."""

from __future__ import annotations

__author__ = "730717721"


class Point:
    """Defining Point class."""
    x: float | int
    y: float | int

    def __init__(self, x_init: float | int = 0.0, y_init: float | int = 0.0):
        """Defining constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method that belongs to the Point class and mutates a Point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Method that belongs to the Point class and creates a new Point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Print out the points in a readable way."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output

    def __mul__(self, factor: int | float) -> Point:
        """Multiplication operator overload."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Addition operator overload."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point