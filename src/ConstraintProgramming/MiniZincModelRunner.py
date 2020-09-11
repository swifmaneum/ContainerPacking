from minizinc import Instance, Solver

from ConstraintProgramming.ModelData import ModelData
from Runner import Runner
from Solution import Solution

backup_solver = "gecode"


class MiniZincModelRunner(Runner):
    def __init__(self, model, solver_name):
        self.model = model
        try:
            self.solver = Solver.lookup(solver_name)
        except LookupError:
            print(f"Solver {solver_name} not found. Falling back to {backup_solver}")
            self.solver = Solver.lookup(backup_solver)

    def find_solution(self, data):
        model_data = ModelData(data["modules"], data["parts"])
        instance = Instance(self.solver, self.model)
        model_data.copy_data_to(instance)
        solution = instance.solve()
        if solution.solution is None or solution["allocation"] is None:
            return None
        else:
            return solution
