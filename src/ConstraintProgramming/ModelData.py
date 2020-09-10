class ModelData(object):

    def __init__(self, modules, parts):
        self.n_parts = len(parts)
        self.lengths = list(map(lambda part: part.length, parts))
        self.widths = list(map(lambda part: part.width, parts))
        self.weights = list(map(lambda part: 1, parts))
        self.groups = list(map(lambda part: part.group, parts))

        self.n_modules = len(modules)
        self.module_lengths = list(map(lambda module: module.length, modules))
        self.module_widths = list(map(lambda module: module.width, modules))
        self.module_juts = list(map(lambda module: module.jut, modules))
        self.module_capacity = list(map(lambda module: module.capacity, modules))

    def copy_data_to(self, instance):
        for key, value in instance.input.items():
            instance[key] = getattr(self, key)
        return instance
