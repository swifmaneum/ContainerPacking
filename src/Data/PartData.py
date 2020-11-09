import itertools
from DataModels.Part import Part


class PartData(object):

    @staticmethod
    def repeat(list_to_repeat, times):
        return list(itertools.chain.from_iterable(itertools.repeat(list_to_repeat, times)))

    @staticmethod
    def get_demo_parts(count=1):
        parts = [
            Part(22000, 5800,  1), Part(22000, 5800, 1), Part(5620, 5600, 2), Part(5620, 5600, 2), Part(5620, 5600, 1),
            Part(22000, 5740, 1), Part(5775, 5960, 4), Part(12340, 5960, 4), Part(5960, 3725, 3)
        ]
        return PartData.repeat(parts, count)

    @staticmethod
    def get_demo_parts_2():
        return PartData.get_hochschrank_1() \
               + PartData.get_oberschrank_1() \
               + PartData.get_unterschrank_4() \
               + PartData.get_hochschrank_1()
        # + PartData.get_traverse(100)

    @staticmethod
    def get_hochschrank_1(count=1, group=1):
        parts = [
            Part(5800, 22000, group), Part(22000, 5800, group), Part(5620, 5600, group), Part(5620, 5600, group),
            Part(5620, 5600, group), Part(22000, 5740, group), Part(5775, 5960, group), Part(12340, 5960, group),
            Part(5960, 3725, group)
        ]
        return PartData.repeat(parts, count)

    @staticmethod
    def get_oberschrank_1(count=1, group=1):
        parts = [
            Part(7000, 3200, group), Part(7000, 3200, group), Part(7620, 2900, group), Part(7620, 2900, group),
            Part(7740, 6000,  group),  # TODO: 7000
            Part(7610, 2800, group), Part(6920, 3960, group), Part(6920, 3960, group)
        ]
        return PartData.repeat(parts, count)

    @staticmethod
    def get_oberschrank_2(count=1, group=1):
        parts = [
            Part(7000, 3200, group), Part(7000, 3200, group), Part(3620, 2900, group), Part(3620, 2900, group),
            Part(7000, 374, group), Part(6920, 500, group), Part(6920, 500, group)
        ]
        return PartData.repeat(parts, count)

    @staticmethod
    def get_unterschrank_4(count=1, group=1):
        parts = [
            Part(7620, 5800, group), Part(7620, 5800, group), Part(5620, 800, group), Part(5620, 5600, group),
            Part(5620, 5600, group), Part(7620, 5740, group), Part(5960, 1575, group), Part(4800, 655, group),
            Part(4915, 5300, group),
        ]
        return PartData.repeat(parts, count)

    @staticmethod
    def get_traverse(count=1, group=1):
        traverse = Part(5620, 800, group)
        return list(itertools.repeat(traverse, count))
