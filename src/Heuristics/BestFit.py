from Heuristics.BaseHeuristic import BaseHeuristic
from Heuristics.HeuristicsHelper import get_best_fitting_module


class BestFit(BaseHeuristic):

    def get_fitting_module(self, part, modules):
        return get_best_fitting_module(part, modules)
