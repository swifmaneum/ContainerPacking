from Module import Module
from Part import Part


class DataSets(object):

    @staticmethod
    def get_demo_parts():
        return [
            Part(5800, 22000), Part(22000, 5800), Part(5620, 5600), Part(5620, 5600), Part(5620, 5600),
            Part(22000, 5740), Part(5775, 5960), Part(12340, 5960), Part(5960, 3725)
        ]

    @staticmethod
    def get_demo_modules():
        return [
            Module(22000, 6000, 3), Module(6000, 6000, 4), Module(14000, 6000, 2)
        ]

    @staticmethod
    def get_container_modules():
        """Modules taken from Jens Töpfers bachelor thesis, see Table 5 on page 29"""
        length = 6000
        jut = 2000
        return [
            Module(length, 14200, 4, jut), Module(length, 900, 5), Module(length, 900, 5),
            Module(length, 20000, 4, jut), Module(length, 8900, 8), Module(length, 3200, 8, jut),
            Module(length, 12500, 8, jut)
        ]
