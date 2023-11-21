"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730717721"


class Simpy:
    """Define Simpy class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Define Simpy Constructor."""
        self.values = values

    def __str__(self) -> str:
        """Define str method."""
        return f"Simpy({self.values})"
    
    def fill(self, val_list: float, num_values: int) -> None:
        """Define fill method."""
        self.values = [val_list] * num_values
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Define arange method."""
        assert step != 0.0
        current_val = start
        
        while (step > 0 and current_val < stop) or (step < 0 and current_val > stop):
            self.values.append(current_val)
            current_val += step

    def sum(self) -> float:
        """Define sum method."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Define __add__ operator overload."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            vals = [self.values[i] + rhs.values[i] for i in range(len(self.values))]
        elif isinstance(rhs, float):
            vals = [value + rhs for value in self.values]
        return Simpy(vals)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Define __pow__ operator overload."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            vals = [self.values[i] ** rhs.values[i] for i in range(len(self.values))]
        elif isinstance(rhs, float):
            vals = [value ** rhs for value in self.values]
        return Simpy(vals)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Define __eq__ operator overload."""
        if isinstance(rhs, Simpy):
            return [self.values[i] == rhs.values[i] for i in range(len(self.values))]
        elif isinstance(rhs, float):
            return [value == rhs for value in self.values]
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Define __gt__ operator overload."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            bool_vals = [self.values[i] > rhs.values[i] for i in range(len(self.values))]
        elif isinstance(rhs, float):
            bool_vals = [value > rhs for value in self.values]
        return bool_vals
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Define __getitem__ operator overload."""
        if isinstance(rhs, int):
            return self.values[rhs]
        elif isinstance(rhs, list):
            assert len(rhs) == len(self.values)
            return Simpy([self.values[i] for i in range(len(self.values)) if rhs[i]])