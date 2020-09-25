from Runner import Runner
from Solution import Solution


class DeepReinforcementLearningRunner(Runner):

    def find_solution(self, data):
        # copy data to instance

        # solve the instance
        solution = None
        if solution.solution is None or solution["allocation"] is None:
            return None
        else:
            own_solution = Solution()
            own_solution.allocation = solution["allocation"]
            own_solution.wasted_space_sum = solution["wasted_space_sum"]
            return own_solution
