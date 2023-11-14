"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730717721"


class River:
    """Defining River class."""
    day: int
    bears: list[Fish] = []
    fish: list[Bear] = []
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Defining check_ages."""
        return None

    def bears_eating(self):
        """Defining bears_eating."""
        return None
    
    def check_hunger(self):
        """Defining check_hunger."""
        return None
        
    def repopulate_fish(self):
        """Defining repopulate_fish."""
        return None
    
    def repopulate_bears(self):
        """Defining repopulate_bears."""
        return None
    
    def view_river(self):
        """Defining view_river."""
        fish_pop = len(self.fish)
        bear_pop = len(self.bears)

        print(f"~~~ Day {self.day} ~~~")
        print(f"Fish population: {fish_pop}")
        print(f"Bear population: {bear_pop}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Simulate one week of life in the river."""
        for elem in range(7):
            self.one_river_day()
            return None