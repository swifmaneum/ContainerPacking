import random

from DataModels.Part import Part
from Data.ModuleData import ModuleData

class RandomProblemGenerator(object):
    def __init__(self, random_seed):
        random.seed(random_seed)

    def __iter__(self):
        return self

    def __next__(self):
        modules = ModuleData.get_container_modules(1)

        change_board_geometry_generation = random.randint(0, 3)
        container_border_values = random.randint(0, 4)
        if change_board_geometry_generation == 0:
            next_part = Part(random.randint(40, 22000), random.randint(40, 6000),  1)
        elif change_board_geometry_generation == 1:
            next_part = Part(random.randint(40, 6000), random.randint(40, 22000), 1)
        elif change_board_geometry_generation == 2:
            next_part = Part((modules[container_border_values].length + 5), (modules[container_border_values].width -1), 1)
        elif change_board_geometry_generation == 3:
            next_part = Part((modules[container_border_values].length - 5), (modules[container_border_values].width -1), 1)
        return [next_part]
