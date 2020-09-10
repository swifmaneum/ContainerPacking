class Solution(object):
    def __init__(self, minizinc_result=None):
        if minizinc_result is None:
            self.allocation = []
            self.wasted_space_sum = 0
        else:
            self.allocation = minizinc_result.solution.allocation
            self.wasted_space_sum = minizinc_result.solution.wasted_space_sum

    def __getitem__(self, key):
        return getattr(self, key)
