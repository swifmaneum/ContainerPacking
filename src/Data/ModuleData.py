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
        width = 6000
        standard_modules = [
            Module(900, width, 0 * container_count), Module(5200, width, 8 * container_count),
            Module(10900, width, 8 * container_count), Module(14500, width, 2 * container_count),
            Module(16200, width, 2 * container_count), Module(22000, width, 3 * container_count),
        ]
        return standard_modules
