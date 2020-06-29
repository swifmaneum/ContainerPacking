from Data.PartData import PartData


class RealisticProblemGenerator(object):
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        available_parts = {
            0: PartData.get_oberschrank_1(),
            1: PartData.get_oberschrank_2(),
            2: PartData.get_hochschrank_1(),
            3: PartData.get_unterschrank_4()
        }
        result = available_parts[self.current % len(available_parts)]
        self.current += 1
        return result
