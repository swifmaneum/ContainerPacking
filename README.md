# ContainerPacking
## Installation

Running our evaluation requires:
- [MiniZinc](https://www.minizinc.org/) 2.5.0 (or higher): Tested with MiniZinc 2.5.1 and 2.5.2
- Python 3.6 (or higher): Tested with Python 3.7

After the installation of MiniZinc and Python, run
```
cd Constraints4Packing
pip install requirements.txt
```

For the best results with the constraint models, use the [Gurobi solver](https://www.gurobi.com/). Free academic licenses are available 
[here](https://www.gurobi.com/academia/academic-program-and-licenses/). Solver preferences can be edited in `Starter.py`

## Running
Edit the `Starter.py` according to your preferences, e.g., (un-) comment the algorithms to test:
```
algorithms_to_test = [
    (BestFit(), "Best Fit"),
    (MiniZincModelRunner(minizinc_model, solver_name), "MiniZinc - Gurobi"),
    (DeepQNetworkRunner(), "DQN")
]
```
Or choose a different problem generator:
```
problem_generator = RandomProblemGenerator(1)
```

After you're done, run the `Starter.py`
