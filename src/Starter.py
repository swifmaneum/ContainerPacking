from minizinc import Model

from Data.ModuleData import ModuleData
from Data.PartData import PartData
from Helper import Helper
from MiniZincModelRunner import MiniZincModelRunner
from Plotter import Plotter

solver_name = "gurobi"
satisfaction_model = Model("./MiniZincModels/BinPacking.mzn")
optimization_model = Model("./MiniZincModels/BinPacking.mzn")
optimization_model.add_file("./MiniZincModels/BinPackingMinimalWastedSpace.mzn")
# model.add_file("./MiniZincModels/BinPackingMaxGroup.mzn")

x = []
y = []
for i in range(1, 51):

    parts = PartData.get_oberschrank_1(i)
    min_number_of_containers = Helper.find_min_number_of_containers(satisfaction_model, solver_name, parts,
                                                                    ModuleData.get_container_modules())

    modules = ModuleData.get_container_modules(min_number_of_containers)
    data = {"modules": modules, "parts": parts}

    print(f"Packing {len(parts)} parts into {min_number_of_containers} containers with {len(modules)} modules")

    result = MiniZincModelRunner(optimization_model, solver_name).run(data)

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
