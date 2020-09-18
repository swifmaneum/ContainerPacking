from AgentClasses.Models.module import Module


class Container:
    def __init__(self, module0_max_length, module0_max_width, module0_max_capacity,
                 module1_max_length, module1_max_width, module1_max_capacity,
                 module2_max_length, module2_max_width, module2_max_capacity,
                 module3_max_length, module3_max_width, module3_max_capacity,
                 module4_max_length, module4_max_width, module4_max_capacity,
                 module5_max_length, module5_max_width, module5_max_capacity):
        self.module0 = Module(0, module0_max_length, module0_max_width, module0_max_capacity)
        self.module1 = Module(1, module1_max_length, module1_max_width, module1_max_capacity)
        self.module2 = Module(2, module2_max_length, module2_max_width, module2_max_capacity)
        self.module3 = Module(3, module3_max_length, module3_max_width, module3_max_capacity)
        self.module4 = Module(4, module4_max_length, module4_max_width, module4_max_capacity)
        self.module5 = Module(5, module5_max_length, module5_max_width, module5_max_capacity)
        self.modules = [self.module0, self.module1, self.module2, self.module3, self.module4, self.module5]

    def update_module_capacities(self, np_random):
        self.modules[0].capacity = np_random.randint(0, self.modules[0].max_capacity)
        self.modules[1].capacity = np_random.randint(0, self.modules[1].max_capacity)
        self.modules[2].capacity = np_random.randint(0, self.modules[2].max_capacity)
        self.modules[3].capacity = np_random.randint(0, self.modules[3].max_capacity)
        self.modules[4].capacity = np_random.randint(0, self.modules[4].max_capacity)
        self.modules[5].capacity = np_random.randint(0, self.modules[5].max_capacity)
