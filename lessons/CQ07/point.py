"""CQ07."""

from __future__ import annotations

__author__ = "730717721"


class Point:
    """Defining Point class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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