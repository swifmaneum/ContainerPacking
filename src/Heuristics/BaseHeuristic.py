from abc import abstractmethod

from Runner import Runner
from Solution import Solution


class BaseHeuristic(Runner):
    def find_solution(self, data):
        parts = data["parts"]
        modules = data["modules"]
        solution = Solution()
        solution.allocation = [None] * len(parts)
        parts = self.preprocess_parts(parts)

        for part in parts:
            fitting_module, wasted_space = self.get_fitting_module(part, modules)
            if fitting_module is None:
                return None
            index_of_best_fit = modules.index(fitting_module)
            solution.allocation[parts.index(part)] = index_of_best_fit
            solution.wasted_space_sum = solution.wasted_space_sum + wasted_space
            modules[index_of_best_fit].capacity = modules[index_of_best_fit].capacity - 1
        return solution

    @abstractmethod
    def get_fitting_module(self, part, modules):
        raise NotImplementedError

    def preprocess_parts(self, parts):
        # Optional method to be overridden by subclasses to do pre-processing, such as sorting
        # If no pre-processing is required, simply do not override this method
        return parts

    @staticmethod
    def part_fits_in_module(part, module):
        return (module.length >= part.length and module.width >= part.width) or (
                module.length >= part.width and module.width >= part.length)

    @staticmethod
    def calculate_wasted_space(part, module):
        return module.length * module.width - part.width * part.length

    @staticmethod
    def get_best_fitting_module(part, modules):
        # Filter out all modules, that the part won't fit in
        feasible_modules = BaseHeuristic.get_feasible_modules(part, modules)
        modules_to_wasted_space = {}
        for module in feasible_modules:
            wasted_space = BaseHeuristic.calculate_wasted_space(part, module)
            modules_to_wasted_space[module] = wasted_space
        if len(modules_to_wasted_space) == 0:
            # If no fitting module exists, return none
            return None, None
        else:
            result = min(modules_to_wasted_space, key=modules_to_wasted_space.get)
            return result, modules_to_wasted_space[result]

    @staticmethod
    def get_first_fitting_module(part, modules):
        feasible_modules = BaseHeuristic.get_feasible_modules(part, modules)
        first_module = next(feasible_modules, None)
        if first_module:
            return first_module, BaseHeuristic.calculate_wasted_space(part, first_module)
        else:
            # If no fitting module exists, return none
            return None, None

    @staticmethod
    def get_feasible_modules(part, modules):
        # Filter out all modules, that the part won't fit in
        return filter(lambda module: BaseHeuristic.part_fits_in_module(part, module) and module.capacity > 0, modules)
