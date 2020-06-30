from datetime import datetime

from minizinc import Result, Status

from Runner import Runner
from Solution import Solution


class BestFitDecreasing(Runner):
    def run(self, data):
        parts = data["parts"]
        modules = data["modules"]
        start = datetime.now()
        solution = Solution()
        sorted_parts = sorted(parts, key=lambda part: part.width * part.length, reverse=True)

        for part in sorted_parts:
            # Filter out all modules, that the part won't fit in
            filtered_modules = filter(
                lambda module: (module.length >= part.length and module.width + module.jut >= part.width)
                               or (module.length >= part.width and module.width + module.jut >= part.length), modules)
            # Calculate the wasted space per module
            wasted_space = list(
                map(lambda module: module.length * (module.width + module.jut) - part.width * part.length,
                    filtered_modules))
            # Get the minimum wasted space, that is greater or equal to zero
            least_wasted_space = min(i for i in wasted_space if i >= 0)
            best_fit = wasted_space.index(least_wasted_space)
            # TODO: Undo sorting!
            solution.allocation.append(best_fit)
            solution.wasted_space_sum = solution.wasted_space_sum + least_wasted_space
            if modules[best_fit].capacity == 1:
                modules.remove(modules[best_fit])
            else:
                modules[best_fit].capacity = modules[best_fit].capacity - 1

        stop = datetime.now()
        statistics = {"time": stop - start}
        return Result(Status.SATISFIED, solution, statistics)
