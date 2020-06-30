from datetime import datetime

from minizinc import Result, Status

from Runner import Runner
from Solution import Solution


class BestFitDecreasing(Runner):
    def run(self, data):
        parts = data["parts"]
        modules = data["modules"]
        # TODO: Add exacter timer
        start = datetime.now()
        solution = Solution()
        solution.allocation = [None] * len(parts)
        sorted_parts = sorted(parts, key=lambda part: part.width * part.length, reverse=True)

        for part in sorted_parts:
            best_fit, wasted_space = self.get_best_fitting_module(part, modules)
            index_of_best_fit = modules.index(best_fit)
            solution.allocation[parts.index(part)] = index_of_best_fit
            solution.wasted_space_sum = solution.wasted_space_sum + wasted_space
            if modules[index_of_best_fit].capacity == 1:
                modules.remove(modules[index_of_best_fit])
            else:
                modules[index_of_best_fit].capacity = modules[index_of_best_fit].capacity - 1

        stop = datetime.now()
        statistics = {"time": stop - start}
        return Result(Status.SATISFIED, solution, statistics)

    def get_best_fitting_module(self, part, modules):
        # Filter out all modules, that the part won't fit in
        feasible_modules = filter(lambda module: self.part_fits_in_module(part, module), modules)
        modules_to_wasted_space = {}
        for module in feasible_modules:
            wasted_space = self.calculate_wasted_space(part, module)
            modules_to_wasted_space[module] = wasted_space
        result = min(modules_to_wasted_space, key=modules_to_wasted_space.get)
        return result, modules_to_wasted_space[result]

    def part_fits_in_module(self, part, module):
        return (module.length >= part.length and module.width + module.jut >= part.width) or (
                module.length >= part.width and module.width + module.jut >= part.length)

    def calculate_wasted_space(self, part, module):
        return module.length * (module.width + module.jut) - part.width * part.length
