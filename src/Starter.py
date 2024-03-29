from Helper import Helper
from minizinc import Model
from Plotter import Plotter
from Data.ModuleData import ModuleData
from Heuristics.BestFit import BestFit
from DataCollector import DataCollector
from ConstraintProgramming.MiniZincModelRunner import MiniZincModelRunner
from ProblemGenerators.RandomProblemGenerator import RandomProblemGenerator
from DeepReinforcementLearning.DeepQNetworkRunner import DeepQNetworkRunner

solver_name = "gurobi"  # gecode, gurobi

minizinc_model = Model(["./ConstraintProgramming/MiniZincModels/BinPackingFloat.mzn"])

algorithms_to_test = [
    # (BestFit(), "Best Fit"),
    # (MiniZincModelRunner(minizinc_model, solver_name), "MiniZinc - Gurobi"),
    (DeepQNetworkRunner(), "DQN")
]

plot = Plotter()
runtime_figure = plot.add_figure("Runtime", "Number of Parts", "Runtime in seconds")
quality_figure = plot.add_figure("Solution Quality", "Number of Parts", "Wasted Space in mm^2")

for model_runner, model_name in algorithms_to_test:
    data_collector = DataCollector(True)

    min_number_of_containers = 1

    problem_generator = RandomProblemGenerator(2)

    parts = []
    for i in range(1, 200):

        parts = parts + next(problem_generator)

        min_number_of_containers = Helper.find_min_number_of_containers(parts, ModuleData.get_container_modules(),
                                                                        min_number_of_containers)
        modules = ModuleData.get_container_modules(min_number_of_containers)
        data = {"modules": modules, "parts": parts}

        print(f"Packing {len(parts)} parts into {min_number_of_containers} containers with {len(modules)} modules")

        result = model_runner.run(data)
        if result.solution is not None:
            print(f"Solved with {model_name} in: {result.statistics['time']}")
            print(result.solution.allocation)
            data_collector.collect(parts, result)

        else:
            print("No solution found")

    plot.add_line(data_collector.get_data("time"), model_name, runtime_figure)
    plot.add_line(data_collector.get_data("wasted_space_sum"), model_name, quality_figure)

    # plot.to_csv(solution_quality_data, model_name)

plot.show()
