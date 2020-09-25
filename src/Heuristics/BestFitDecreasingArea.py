from Heuristics.BaseHeuristic import BaseHeuristic


class BestFitDecreasingArea(BaseHeuristic):
    def get_fitting_module(self, part, modules):
        return BaseHeuristic.get_best_fitting_module(part, modules)

    def preprocess_parts(self, parts):
        return sorted(parts, key=lambda part: part.length * part.width, reverse=True)
