from Module import Module


class ModuleData(object):
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
