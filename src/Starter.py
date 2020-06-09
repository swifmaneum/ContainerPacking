import math

from minizinc import Model

from ModelData import ModelData
from ModelRunner import ModelRunner
from ModuleData import ModuleData
from PartData import PartData

model = Model("./MiniZincModels/BinPacking.mzn")
solver_name = "gurobi"


def find_min_number_of_containers(parts, container_modules):
    number_of_slots = sum(map(lambda module: module.capacity, container_modules))
    min_number_of_containers = math.ceil(len(parts) / number_of_slots)

    result = None

    while result is None or result.solution is None:
        modules = ModuleData.get_container_modules(min_number_of_containers)
        data = ModelData(modules, parts)
        result = ModelRunner(model, solver_name).run(data)

        if result.solution is not None:
            return min_number_of_containers
        else:
            print(f"No solution found with  {min_number_of_containers} containers, increasing container count")
            min_number_of_containers = min_number_of_containers + 1


parts = PartData.get_demo_parts()
min_number_of_containers = find_min_number_of_containers(parts, ModuleData.get_container_modules())

modules = ModuleData.get_container_modules(min_number_of_containers)
data = ModelData(modules, parts)

print(f"Packing {len(parts)} parts into {min_number_of_containers} containers with {len(modules)} modules")

model.add_file("./MiniZincModels/BinPackingMaxGroup.mzn")
result = ModelRunner(model, solver_name).run(data)

if result.solution is not None:
    print(f"Solved with {solver_name} in: {result.statistics['time']}")
    print(result.solution.allocation)
    if hasattr(result.solution, 'wasted_space'):
        print(result.solution.wasted_space)
    if hasattr(result.solution, 'objective'):
        print(result.solution.objective)
else:
    print("No solution found")
