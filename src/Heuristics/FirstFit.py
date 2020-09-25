from Heuristics.BaseHeuristic import BaseHeuristic


class FirstFit(BaseHeuristic):
    def get_fitting_module(self, part, modules):
        return BaseHeuristic.get_first_fitting_module(part, modules)
