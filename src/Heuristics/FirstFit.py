from Heuristics.BaseHeuristic import BaseHeuristic
from Heuristics.HeuristicsHelper import get_first_fitting_module


class FirstFit(BaseHeuristic):
    def get_fitting_module(self, part, modules):
        return get_first_fitting_module(part, modules)
