from Heuristics.BaseHeuristic import BaseHeuristic


class FirstFitDecreasing(BaseHeuristic):
    def get_fitting_module(self, part, modules):
        return BaseHeuristic.get_first_fitting_module(part, modules)

    def preprocess_parts(self, parts):
        return sorted(parts, key=lambda part: max(part.length, part.width), reverse=True)
