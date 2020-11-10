import itertools
from DataModels.Part import Part


class PartData(object):

    @staticmethod
    def repeat(list_to_repeat, times):
        return list(itertools.chain.from_iterable(itertools.repeat(list_to_repeat, times)))

    @staticmethod
    def get_demo_parts(count=1):
        parts = [
            Part(2200.0, 580.0, 1), Part(2200.0, 580.0, 1), Part(562.0, 560.0, 2), Part(562.0, 560.0, 2),
            Part(562.0, 560.0, 1), Part(2200.0, 574.0, 1), Part(577.5, 596.0, 4), Part(1234.0, 596.0, 4),
            Part(596.0, 372.5, 3)
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
            Part(580.0, 2200.0, group), Part(2200.0, 580.0, group), Part(562.0, 560.0, group),
            Part(562.0, 560.0, group),
            Part(562.0, 560.0, group), Part(2200.0, 574.0, group), Part(577.5, 596.0, group),
            Part(1234.0, 596.0, group),
            Part(596.0, 372.5, group)
        ]
        return PartData.repeat(parts, count)

    @staticmethod
    def get_oberschrank_1(count=1, group=1):
        parts = [
            Part(700.0, 320.0, group), Part(700.0, 320.0, group), Part(762.0, 290.0, group), Part(762.0, 290.0, group),
            Part(774.0, 600.0, group),  # TODO: 7000
            Part(761.0, 280.0, group), Part(692.0, 396.0, group), Part(692.0, 396.0, group)
        ]
        return PartData.repeat(parts, count)

    @staticmethod
    def get_oberschrank_2(count=1, group=1):
        parts = [
            Part(700.0, 320.0, group), Part(700.0, 320.0, group), Part(362.0, 290.0, group), Part(362.0, 290.0, group),
            Part(700.0, 37.4, group), Part(692.0, 50.0, group), Part(692.0, 50.0, group)
        ]
        return PartData.repeat(parts, count)

    @staticmethod
    def get_unterschrank_4(count=1, group=1):
        parts = [
            Part(762.0, 580.0, group), Part(762.0, 580.0, group), Part(562.0, 80.0, group), Part(562.0, 560.0, group),
            Part(562.0, 560.0, group), Part(762.0, 574.0, group), Part(596.0, 157.5, group), Part(480.0, 65.5, group),
            Part(491.0, 530.0, group),
        ]
        return PartData.repeat(parts, count)

    @staticmethod
    def get_traverse(count=1, group=1):
        traverse = Part(562.0, 80.0, group)
        return list(itertools.repeat(traverse, count))
