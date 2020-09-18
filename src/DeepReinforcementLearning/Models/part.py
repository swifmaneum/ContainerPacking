class Part:
    def __init__(self, np_random, min_length, max_length, min_width, max_width):
        self.length = np_random.randint(min_length, max_length)
        self.width = np_random.randint(min_width, max_width)
