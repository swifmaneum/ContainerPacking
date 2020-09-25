import copy

import gym
import numpy as np
from gym import spaces
from gym.utils import seeding

from DeepReinforcementLearning.AgentEnvironmentClasses.aiRuleBase import is_best_fitting_module


class ProblemGeneratorEnv(gym.Env):

    def __init__(self, problem_data):
        self.problem_data = problem_data
        self.parts = copy.deepcopy(self.problem_data["parts"])
        self.modules = copy.deepcopy(self.problem_data["modules"])
        self.part = None
        self.current_part_index = 0
        self.reward = 0
        self.next_environment_observation = ()
        # Allow the length of modules as actions, + 1 for 'no module available'
        self.action_space = spaces.Discrete(len(self.modules) + 1)

        observation_space_low = np.array([40, 40])
        observation_space_high = np.array([2000, 600])
        for _ in self.modules:
            # Lower bound is 0, indicating there is no capacity in the module
            observation_space_low = np.append(observation_space_low, 0)
            # Upper bound is 1, indicating there is still capacity in the module
            observation_space_high = np.append(observation_space_high, 1)
        self.observation_space = spaces.Box(low=observation_space_low, high=observation_space_high, dtype=np.uint64)
        self.np_random = ()
        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)
        # Decrease the action value (1-indexed) by one to map it to python list indices (0-indexed)
        action_index = action - 1
        # print(action_index)

        if is_best_fitting_module(action_index, self.part, self.modules):
            self.reward = 1
        else:
            self.reward = 0

        # If we did not choose 'no module available' and there's still capacity in the chosen module
        if action != len(self.modules) + 1 and self.modules[action_index].capacity > 0:
            # Decrease the capacity of the chosen module
            self.modules[action_index].capacity = self.modules[action_index].capacity - 1

        self.current_part_index = self.current_part_index + 1
        if self.current_part_index == len(self.parts):
            # If we've reached the last part, end the episode by returning done is true
            return np.empty(9), self.reward, True, {}
        else:
            # Else return the next part and continue the episode
            self.part = self.parts[self.current_part_index]
            self.next_environment_observation = self.build_observation(self.part)
            return self.next_environment_observation, self.reward, False, {}

    def reset(self):
        self.modules = copy.deepcopy(self.problem_data["modules"])
        self.current_part_index = 0
        self.part = self.parts[self.current_part_index]
        self.next_environment_observation = self.build_observation(self.part)
        return self.next_environment_observation

    def build_observation(self, part):
        part_dimensions = (part.length, part.width)
        module_capacities = []
        for module in self.modules:
            module_capacities.append(1 if module.capacity > 0 else 0)

        return np.array(part_dimensions + tuple(module_capacities))
