import random

from DataModels.Part import Part


class RandomProblemGenerator(object):
    def __init__(self, random_seed):
        random.seed(random_seed)

    def __iter__(self):
        return self

    def __next__(self):
        next_part = Part(random.randint(10, 6000), random.randint(10, 20000), 1)
        print(next_part.length, next_part.width)
        return [next_part]
