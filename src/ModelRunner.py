from minizinc import Instance, Model, Solver

from DataSets import DataSets
from ModelData import ModelData

model = Model("./MiniZincModels/BinPacking.mzn")
solver = Solver.lookup("gecode")
instance = Instance(solver, model)

modules = DataSets.get_demo_modules()
parts = DataSets.get_demo_parts()
data = ModelData(modules, parts)
data.copy_data_to(instance)

print("Solving with " + solver.name + " ...")
result = instance.solve()

if result.solution is not None:
    print("Solved in: " + str(result.statistics["time"]))
    print(result.solution.allocation)
    if hasattr(result.solution, 'wasted_space'):
        print(result.solution.wasted_space)
    if hasattr(result.solution, 'objective'):
        print(result.solution.objective)
else:
    print("No solution found")
