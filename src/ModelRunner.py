from minizinc import Instance, Model, Solver

from ModuleData import ModuleData
from PartData import PartData
from ModelData import ModelData

model = Model("./MiniZincModels/BinPacking.mzn")
solver = Solver.lookup("gecode")
instance = Instance(solver, model)

modules = ModuleData.get_container_modules()
parts = PartData.get_demo_parts_2()
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
