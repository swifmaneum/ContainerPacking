import time
from abc import ABC, abstractmethod
from datetime import timedelta

from minizinc import Result, Status


class Runner(ABC):

    def run(self, data):
        start = time.time_ns()
        solution = self.find_solution(data)
        stop = time.time_ns()
        nanoseconds = stop - start
        statistics = {"time": timedelta(seconds=nanoseconds / (10 ** 9))}

        if isinstance(solution, Result):
            # If the solution is already a MiniZinc Result, simply return it
            return solution
        # Otherwise wrap the solution into a MiniZinc Result to have a consistent interface
        return Result(Status.SATISFIED, solution, statistics)

    @abstractmethod
    def find_solution(self, data):
        raise NotImplementedError
