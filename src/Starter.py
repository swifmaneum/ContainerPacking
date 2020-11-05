import numpy as np
from minizinc import Model

from DataCollector import DataCollector
from DataModels.Part import Part
from DeepReinforcementLearning.DeepQNetworkRunner import DeepQNetworkRunner
from Heuristics.BestFit import BestFit
from Heuristics.BestFitDecreasing import BestFitDecreasing
from Data.ModuleData import ModuleData
from Helper import Helper
from ConstraintProgramming.MiniZincModelRunner import MiniZincModelRunner
from Heuristics.BestFitDecreasingArea import BestFitDecreasingArea
from Heuristics.FirstFit import FirstFit
from Plotter import Plotter
from ProblemGenerators.RandomProblemGenerator import RandomProblemGenerator
from ProblemGenerators.RealisticProblemGenerator import RealisticProblemGenerator

solver_name = "chuffed"  # gecode, chuffed, gurobi
satisfaction_model = Model("./ConstraintProgramming/MiniZincModels/BinPacking.mzn")
formal_model = Model(["./ConstraintProgramming/MiniZincModels/BinPackingFormalModel.mzn"])
minimal_space_model = Model(["./ConstraintProgramming/MiniZincModels/BinPacking.mzn",
                             "./ConstraintProgramming/MiniZincModels/BinPackingMinimalWastedSpace.mzn"])

algorithms_to_test = [
    (BestFit(), "Best Fit"),
    # (FirstFit(), "First Fit"),
    # (BestFitDecreasing(), "Best Fit Decreasing"),
    # (MiniZincModelRunner(satisfaction_model, solver_name), "Satisfaction model"),
    # (MiniZincModelRunner(formal_model, solver_name), "Formal model"),
    # (MiniZincModelRunner(minimal_space_model, solver_name), "Minimal space model"),
    (DeepQNetworkRunner(), "DQN")
]

plot = Plotter()
runtime_figure = plot.add_figure("Laufzeit", "Anzahl Teile", "Laufzeit in Sekunden")
quality_figure = plot.add_figure("Lösungsqualität", "Anzahl Teile", "Verschwendeter Platz in mm^2")
grouped_items_figure = plot.add_figure("Lösungsqualität", "Anzahl Teile", "Anzahl gruppierter Teile")

for model_runner, model_name in algorithms_to_test:
    data_collector = DataCollector(True)

    min_number_of_containers = 1
    # problem_generator = RealisticProblemGenerator()
    problem_generator = RandomProblemGenerator(1250) #1250/2500 works for 100 / 5000 works for 80 boards
    # parts = [Part(950, 950, 1)]
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
    plot.add_line(data_collector.get_data("grouped_parts"), model_name, grouped_items_figure)

    # plot.to_csv(solution_quality_data, model_name)

plot.show()
