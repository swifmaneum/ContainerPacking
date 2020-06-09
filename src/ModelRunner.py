from minizinc import Instance, Solver

backup_solver = "gecode"


class ModelRunner(object):
    def __init__(self, model, solver_name):
        self.model = model
        try:
            self.solver = Solver.lookup(solver_name)
        except LookupError:
            print(f"Solver {solver_name} not found. Falling back to {backup_solver}")
            self.solver = Solver.lookup(backup_solver)

    def run(self, model_data):
        instance = Instance(self.solver, self.model)
        model_data.copy_data_to(instance)
        return instance.solve()
