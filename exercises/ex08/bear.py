"""File to define Bear class."""


class Bear:
    """Defining bear class."""
    age: int
    hunger_score: int
    
    def __init__(self):
        """Defining constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Defining one_day for bear."""
        self.age += 1
        return None