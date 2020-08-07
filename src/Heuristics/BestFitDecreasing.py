from Heuristics.BaseHeuristic import BaseHeuristic
from Heuristics.HeuristicsHelper import get_best_fitting_module


class BestFitDecreasing(BaseHeuristic):
    def get_fitting_module(self, part, modules):
        return get_best_fitting_module(part, modules)

    def preprocess_parts(self, parts):
        return sorted(parts, key=lambda part: max(part.length, part.width), reverse=True)
