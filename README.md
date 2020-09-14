# ContainerPacking
## Installation

The [MiniZinc Python interface](https://minizinc-python.readthedocs.io/en/latest/getting_started.html) requires:
- [MiniZinc](https://www.minizinc.org/) 2.3.2 (or higher)
- Python 3.6 (or higher)

After the installation, run
```
cd Constraints4Packing
pip install requirements.txt
```

For the best results with the constraint models, use the Gurobi solver. Free academic licenses are available 
[here](https://www.gurobi.com/academia/academic-program-and-licenses/). Solver preferences can be edited in `Starter.py`

## Running
Edit the `Starter.py` according to your preferences, e.g., (un-) comment the algorithms to test:
```
algorithms_to_test = [
    (BestFit(), "Best Fit"),
    # (FirstFit(), "First Fit"),
    # (BestFitDecreasing(), "Best Fit Decreasing"),
    # (MiniZincModelRunner(satisfaction_model, solver_name), "Satisfaction model"),
     (MiniZincModelRunner(formal_model, solver_name), "Formal model"),
    # (MiniZincModelRunner(minimal_space_model, solver_name), "Minimal space model"),
    # (MiniZincModelRunner(group_model, solver_name), "Groupping model"),
]
```
Or choose a different problem generator:
```
problem_generator = RandomProblemGenerator(1)
```

After you're done, run the `Starter.py`
