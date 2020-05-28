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
