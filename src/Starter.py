import math

from minizinc import Model

from DataModels.ModelData import ModelData
from Helper import Helper
from ModelRunner import ModelRunner
from Data.ModuleData import ModuleData
from Data.PartData import PartData
from Plotter import Plotter

satisfaction_model = Model("./MiniZincModels/BinPacking.mzn")
solver_name = "gurobi"
optimization_model = Model("./MiniZincModels/BinPacking.mzn")
optimization_model.add_file("./MiniZincModels/BinPackingMinimalWastedSpace.mzn")
# model.add_file("./MiniZincModels/BinPackingMaxGroup.mzn")

x = []
y = []
for i in range(1, 26):

    parts = PartData.get_oberschrank_1(i)
    min_number_of_containers = Helper.find_min_number_of_containers(satisfaction_model, solver_name, parts,
                                                                    ModuleData.get_container_modules())

    modules = ModuleData.get_container_modules(min_number_of_containers)
    data = ModelData(modules, parts)

    print(f"Packing {len(parts)} parts into {min_number_of_containers} containers with {len(modules)} modules")

    result = ModelRunner(optimization_model, solver_name).run(data)

    if result.solution is not None:
        print(f"Solved with {solver_name} in: {result.statistics['time']}")
        x.append(len(parts))
        y.append(result.statistics['time'].total_seconds())
        print(result.solution.allocation)
        if hasattr(result.solution, 'wasted_space'):
            print(result.solution.wasted_space)
        if hasattr(result.solution, 'objective'):
            print(result.solution.objective)
    else:
        print("No solution found")

Plotter(x, y).show()
