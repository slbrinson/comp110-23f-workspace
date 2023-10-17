"""Summing the elements of a list using different loops."""

__author__ = "730717721"


def w_sum(vals: list[float]) -> float:
    """Sum of the numbers in the list using a while loop."""
    vals_idx: int = 0
    vals_sum: float = 0.0
    while vals_idx < len(vals):
        vals_sum += vals[vals_idx]
        vals_idx += 1
    return vals_sum


def f_sum(vals: list[float]) -> float:
    """Sum of the numbers in the list using a for loop."""
    vals_sum: float = 0.0
    for num in vals:
        vals_sum += num
    return vals_sum


def f_range_sum(vals: list[float]) -> float:
    """Sum of the numbers in the list using a for loop in range."""
    vals_sum: float = 0.0
    for vals_idx in range(len(vals)):
        vals_sum += vals[vals_idx]
    return vals_sum