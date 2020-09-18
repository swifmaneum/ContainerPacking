from DataModels.ModelData import ModelData
from Runner import Runner
from Solution import Solution



class DeepReinforcementLearningRunner(Runner):

    def find_solution(self, data):
        model_data = ModelData(data["modules"], data["parts"])
        instance = Instance(self.solver, self.model)
        model_data.copy_data_to(instance)
        solution = instance.solve()
        if solution.solution is None or solution["allocation"] is None:
            return None
        else:
            own_solution = Solution()
            own_solution.allocation = solution["allocation"]
            own_solution.wasted_space_sum = solution["wasted_space_sum"]
            return own_solution
