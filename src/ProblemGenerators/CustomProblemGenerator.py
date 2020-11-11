from DataModels.Part import Part


class CustomProblemGenerator(object):
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        available_parts = [Part(900, 50),
                           Part(900, 5900)]
        result = available_parts[self.current % len(available_parts)]
        self.current += 1
        return [result]
