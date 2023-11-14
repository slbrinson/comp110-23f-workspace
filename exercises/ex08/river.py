"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730717721"


class River:
    """Defining River class."""
    day: int
    bears: list[Bear] = []
    fish: list[Fish] = []
    
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
        """Removing bears and fish based on their age."""
        surviving_fish_list: list[int] = list()
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish_list.append(fish)
        self.fish = surviving_fish_list

        surviving_bears_list: list[int] = list()
        for bears in self.bears:
            if bears.age <= 5:
                surviving_bears_list.append(bears)
        self.bears = surviving_bears_list
        return None

    def bears_eating(self):
        """Bears will eat three fish if there are at least five fish in the river."""
        fish_for_bears = 5 * len(self.bears)
        if len(self.fish) >= fish_for_bears:
            for bear in self.bears:
                if len(self.fish) >= 5:
                    self.remove_fish(3)
                    bear.eat(3)
        return None
    
    def check_hunger(self):
        """Defining check_hunger."""
        surviving_bears_list: list[int] = list()
        for bears in self.bears:
            if bears.hunger_score >= 0:
                surviving_bears_list.append(bears)
        self.bears = surviving_bears_list
        return None
        
    def repopulate_fish(self):
        """Each set of fish will produce four offspring."""
        new_fish_list: list[int] = list()
        new_fish_num = (len(self.fish) // 2) * 4
        for fish in range(new_fish_num):
            new_fish = Fish()
            new_fish_list.append(new_fish)
        for new_fish in new_fish_list:
            self.fish.append(new_fish)
        return None
    
    def repopulate_bears(self):
        """Each set of bears will produce one offspring."""
        new_bears_list: list[int] = list()
        new_bears_born = len(self.bears) // 2
        for bear in range(new_bears_born):
            new_bears = Bear()
            new_bears_list.append(new_bears)
        for new_bears in new_bears_list:
            self.bears.append(new_bears)
        return None
    
    def view_river(self):
        """Defining view_river."""
        fish_pop = len(self.fish)
        bear_pop = len(self.bears)

        print(f"~~~ Day {self.day}: ~~~")
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
        for day in range(7):
            self.one_river_day()
        return None
        
    def remove_fish(self, amount: int):
        """Removing fish at the first index."""
        for fish in range(amount):
            self.fish.pop(0)
            return None