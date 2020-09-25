class Solution(object):
    def __init__(self):
        self.allocation = []
        self.wasted_space_sum = 0

    def __getitem__(self, key):
        return getattr(self, key)
