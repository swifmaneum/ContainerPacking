import itertools

from Part import Part


class PartData(object):

    @staticmethod
    def get_demo_parts():
        return [
            Part(5800, 22000), Part(22000, 5800), Part(5620, 5600), Part(5620, 5600), Part(5620, 5600),
            Part(22000, 5740), Part(5775, 5960), Part(12340, 5960), Part(5960, 3725)
        ]

    @staticmethod
    def get_demo_parts_2():
        return PartData.get_hochschrank_1() \
               + PartData.get_oberschrank_1() \
               + PartData.get_unterschrank_4() \
               + PartData.get_traverse(10)

    @staticmethod
    def get_hochschrank_1():
        return [
            Part(5800, 22000), Part(22000, 5800), Part(5620, 5600), Part(5620, 5600), Part(5620, 5600),
            Part(22000, 5740), Part(5775, 5960), Part(12340, 5960), Part(5960, 3725)
        ]

    @staticmethod
    def get_oberschrank_1():
        return [
            Part(7000, 3200), Part(7000, 3200), Part(7620, 2900), Part(7620, 2900), Part(6000, 7740),  # TODO: 7000
            Part(7610, 2800), Part(6920, 3960), Part(6920, 3960)
        ]

    @staticmethod
    def get_oberschrank_2():
        return [
            Part(7000, 3200), Part(7000, 3200), Part(3620, 2900), Part(3620, 2900), Part(7000, 374),
            Part(6920, 500), Part(6920, 500)
        ]

    @staticmethod
    def get_unterschrank_4():
        return [
            Part(7620, 5800), Part(7620, 5800), Part(5620, 800), Part(5620, 5600), Part(5620, 5600),
            Part(7620, 5740), Part(5960, 1575), Part(4800, 655), Part(4915, 5300),
        ]

    @staticmethod
    def get_traverse(count=1):
        traverse = Part(5620, 800)
        return list(itertools.repeat(traverse, count))
