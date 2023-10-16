"""Summing the elements of a list using different loops."""

__author__ = "730717721"

def w_sum(vals: list[float]) -> float:
    vals_idx: int = 0
    vals_sum: float = 0.0
    while vals_idx <= len(vals):
        vals_sum += vals[vals_idx]
        vals_idx += 1
        return vals_sum