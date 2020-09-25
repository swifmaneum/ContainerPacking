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
        # Optional method to be overriden by subclasses to do pre-processing, such as sorting
        # If no pre-processing is required, simply do not override this method
        return parts
