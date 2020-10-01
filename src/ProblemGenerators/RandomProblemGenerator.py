import random

from DataModels.Part import Part


class RandomProblemGenerator(object):
    def __init__(self, random_seed):
        random.seed(random_seed)

    def __iter__(self):
        return self

    def __next__(self):
        next_part = Part(random.randint(40, 6000), random.randint(40, 20000), 1)
        return [next_part]
