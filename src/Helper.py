import math

from Data.ModuleData import ModuleData
from Heuristics.BestFit import BestFit


class Helper(object):
    @staticmethod
    def find_min_number_of_containers(model, solver_name, parts, container_modules, hint):
        number_of_slots = sum(map(lambda module: module.capacity, container_modules))
        min_number_of_containers = math.ceil(len(parts) / number_of_slots)

        if hint is not None:
            # Performance tweak:
            # If a hint is provided, choose the max of min_number_of_containers and hint
            min_number_of_containers = max(min_number_of_containers, hint)

        result = None

        while result is None or result.solution is None:
            modules = ModuleData.get_container_modules(min_number_of_containers)
            data = {"modules": modules, "parts": parts}
            result = BestFit().run(data)

            if result.solution is not None:
                return min_number_of_containers
            else:
                print(f"No solution found with  {min_number_of_containers} containers, increasing container count")
                min_number_of_containers = min_number_of_containers + 1
