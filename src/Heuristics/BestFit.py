from Heuristics.BaseHeuristic import BaseHeuristic


class BestFit(BaseHeuristic):

    def get_fitting_module(self, part, modules):
        return BaseHeuristic.get_best_fitting_module(part, modules)
