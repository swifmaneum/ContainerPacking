from DataModels.Module import Module


class ModuleData(object):
    @staticmethod
    def get_demo_modules():
        return [
            Module(2200.0, 600.0, 3), Module(600.0, 600.0, 4), Module(1400.0, 600.0, 2)
        ]

    @staticmethod
    def get_container_modules(container_count=1):
        """Modules taken from Jens Töpfers bachelor thesis, see Table 5 on page 29"""
        width = 600.0
        standard_modules = [
            Module(90.0, width, 12 * container_count), Module(520.0, width, 8 * container_count),
            Module(1090.0, width, 8 * container_count), Module(1450.0, width, 8 * container_count),
            Module(1620.0, width, 4 * container_count), Module(2200.0, width, 4 * container_count),
        ]
        return standard_modules
