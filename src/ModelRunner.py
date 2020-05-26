from minizinc import Instance, Model, Solver

from DataSets import DataSets
from ModelData import ModelData

model = Model("./MiniZincModels/PartAlloc.mzn")
solver = Solver.lookup("gecode")
instance = Instance(solver, model)

slots = DataSets.get_demo_slots()
parts = DataSets.get_demo_parts()
data = ModelData(slots, parts)
data.copy_data_to(instance)

print("Solving with " + solver.name + " ...")
result = instance.solve()

if result.solution is not None:
    print("Solved in: " + str(result.statistics["time"]))
    print(result.solution.allocation)
else:
    print("No solution found")
