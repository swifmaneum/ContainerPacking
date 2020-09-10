from Heuristics.BaseHeuristic import BaseHeuristic
from Heuristics.HeuristicsHelper import get_first_fitting_module


class FirstFitDecreasing(BaseHeuristic):
    def get_fitting_module(self, part, modules):
        return get_first_fitting_module(part, modules)

    def preprocess_parts(self, parts):
        return sorted(parts, key=lambda part: max(part.length, part.width), reverse=True)
