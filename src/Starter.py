from minizinc import Model

from Data.ModuleData import ModuleData
from Helper import Helper
from ConstraintProgramming.MiniZincModelRunner import MiniZincModelRunner
from Plotter import Plotter
from ProblemGenerators.RandomProblemGenerator import RandomProblemGenerator
from ProblemGenerators.RealisticProblemGenerator import RealisticProblemGenerator

solver_name = "gurobi"
satisfaction_model = Model("./ConstraintProgramming/MiniZincModels/BinPacking.mzn")
minimal_space_model = Model("./ConstraintProgramming/MiniZincModels/BinPacking.mzn")
minimal_space_model.add_file("./ConstraintProgramming/MiniZincModels/BinPackingMinimalWastedSpace.mzn")
max_grouping_model = Model("./ConstraintProgramming/MiniZincModels/BinPacking.mzn")
max_grouping_model.add_file("./ConstraintProgramming/MiniZincModels/BinPackingMaxGroup.mzn")

models_to_test = [(satisfaction_model, "Satisfaction model"), (minimal_space_model, "Minimal space model")]
# (max_grouping_model, "Maximal grouping model")]
plot = Plotter()
runtime_figure = plot.add_figure("Laufzeit", "Anzahl Teile", "Laufzeit in Sekunden")
quality_figure = plot.add_figure("Lösungsqualität", "Anzahl Teile", "Verschwendeter Platz in mm^2")

for model, model_name in models_to_test:

    runtime_data = []
    solution_quality_data = []
    min_number_of_containers = 1
    problem_generator = RandomProblemGenerator(1)
    parts = []

    for i in range(1, 51):

        parts = parts + next(problem_generator)

        min_number_of_containers = Helper.find_min_number_of_containers(satisfaction_model, solver_name, parts,
                                                                        ModuleData.get_container_modules(),
                                                                        min_number_of_containers)

        modules = ModuleData.get_container_modules(min_number_of_containers)
        data = {"modules": modules, "parts": parts}

        print(f"Packing {len(parts)} parts into {min_number_of_containers} containers with {len(modules)} modules")

        result = MiniZincModelRunner(model, solver_name).run(data)

        if result.solution is not None:
            print(f"Solved with {solver_name} in: {result.statistics['time']}")
            runtime_data.append((len(parts), result.statistics['time'].total_seconds()))

            print(result.solution.allocation)
            if hasattr(result.solution, 'wasted_space_sum'):
                print(result.solution.wasted_space_sum)
                solution_quality_data.append((len(parts), result.solution.wasted_space_sum))

        else:
            print("No solution found")

    plot.add_line(runtime_data, model_name, runtime_figure)
    plot.add_line(solution_quality_data, model_name, quality_figure)

plot.show()
