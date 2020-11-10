import random
from DataModels.Part import Part


class RandomProblemGenerator(object):
    def __init__(self, random_seed):
        random.seed(random_seed)

    def __iter__(self):
        return self

    def __next__(self):
        if random.randint(0, 1) == 0:
            next_part = Part(round(random.uniform(4, 600), 1), round(random.uniform(4, 2000), 1), 1)
        else:
            next_part = Part(round(random.uniform(4, 2000), 1), round(random.uniform(4, 600), 1), 1)
        return [next_part]
