"""File to define Fish class."""


class Fish:
    """Defining fish class."""
    age: int

    def __init__(self):
        """Defining constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """Defining one_day for fish."""
        self.age += 1
        return None