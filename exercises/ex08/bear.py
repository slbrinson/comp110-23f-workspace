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
        """Defining one_day for bears."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increase hunger score for the num_fish a bear is eating."""
        self.hunger_score += num_fish
        return None