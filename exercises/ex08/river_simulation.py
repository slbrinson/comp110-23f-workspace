"""River simulation."""

from exercises.ex08.river import River

my_river: River = River(10, 2)

for day in range(1, 8):
    my_river.one_river_week()