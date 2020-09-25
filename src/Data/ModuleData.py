from DataModels.Module import Module


class ModuleData(object):
    @staticmethod
    def get_demo_modules():
        return [
            Module(22000, 6000, 3), Module(6000, 6000, 4), Module(14000, 6000, 2)
        ]

    @staticmethod
    def get_container_modules(container_count=1):
        """Modules taken from Jens Töpfers bachelor thesis, see Table 5 on page 29"""
        length = 6000
        jut = 2000
        standard_modules = [
            Module(length, 14200, 4 * container_count, jut), Module(length, 900, 6 * container_count),
            Module(length, 900, 6 * container_count), Module(length, 20000, 4 * container_count, jut),
            Module(length, 8900, 8 * container_count), Module(length, 3200, 8 * container_count, jut),
            Module(length, 12500, 8 * container_count, jut)
        ]
        return standard_modules
