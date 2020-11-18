import gym
import copy
import random
import numpy as np
from gym import spaces
from gym.utils import seeding

from Helper import Helper
from Solution import Solution
from Data.ModuleData import ModuleData
from ProblemGenerators.RandomProblemGenerator import RandomProblemGenerator
from DeepReinforcementLearning.AgentEnvironmentClasses.aiRuleBase import is_best_fitting_module, calculate_wasted_space, \
    part_fits_in_module


class TrainingEnvironment(gym.Env):

    def __init__(self):
        self.episode = 1
        self.problem_data = self.generate_random_data()
        self.episode_finished = False
        self.parts = copy.deepcopy(self.problem_data["parts"])
        self.modules = copy.deepcopy(self.problem_data["modules"])
        self.solution = Solution()
        self.part = None
        self.current_part_index = 0
        self.reward = 0
        self.next_environment_observation = ()
        self.action_space = spaces.Discrete(len(self.modules))
        observation_space_low = np.array([0.0, 0.0])
        observation_space_high = np.array([1.0, 1.0])

        for _ in self.modules:
            # Lower bound is 0, indicating there is no capacity in the module
            observation_space_low = np.append(observation_space_low, 0)
            # Upper bound is 1, indicating there is still capacity in the module
            observation_space_high = np.append(observation_space_high, 1)

        self.observation_space = spaces.Box(low=observation_space_low, high=observation_space_high, dtype=np.float64)
        self.np_random = ()
        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        """
        :type action: Int
        """
        assert self.action_space.contains(action)
        self.solution.allocation.append(action)

        wasted_space = calculate_wasted_space(self.part, self.modules[action])
        self.solution.wasted_space_sum += wasted_space
        self.modules[action].capacity = self.modules[action].capacity - 1

        # if infeasable - reset
        if not self.is_feasable(action, self.part):
            return np.empty(self.observation_space.shape[0]), -1, True, {}

        # else return wasted space as reward
        self.reward = 1000000 / wasted_space

        self.current_part_index = self.current_part_index + 1
        if self.current_part_index == len(self.parts):
            self.episode_finished = True
            print("------------------------------------------")
            print("Finished episode " + str(self.episode))
            self.episode = self.episode + 1
            # If we've reached the last part, end the episode by returning done is true
            return np.empty(self.observation_space.shape[0]), self.reward, True, {}
        else:
            # Else return the next part and continue the episode
            self.part = self.parts[self.current_part_index]
            self.next_environment_observation = self.build_observation(self.part)
            return self.next_environment_observation, self.reward, False, {}

    def reset(self):
        if self.episode_finished:
            # If the episode is finished: generate new random data
            self.problem_data = self.generate_random_data()
        self.episode_finished = False
        self.parts = copy.deepcopy(self.problem_data["parts"])
        self.modules = copy.deepcopy(self.problem_data["modules"])
        self.solution = Solution()
        self.current_part_index = 0
        self.part = self.parts[self.current_part_index]
        self.next_environment_observation = self.build_observation(self.part)
        return self.next_environment_observation

    def build_observation(self, part):
        # Scale the part dimensions to the interval [0,1]
        part_dimensions = (part.length / 2200.0, part.width / 2200.0)

        module_capacities = []
        for module in self.modules:
            module_capacities.append(1 if module.capacity > 0 else 0)
        return np.array(part_dimensions + tuple(module_capacities))

    def generate_random_data(self):
        problem_generator = RandomProblemGenerator(np.random.randint(1, 10000))
        parts = []
        for i in range(self.episode):
            parts = parts + next(problem_generator)

        min_number_of_containers = Helper.find_min_number_of_containers(parts, ModuleData.get_container_modules(), 1)
        modules = ModuleData.get_container_modules(min_number_of_containers)

        return {"modules": modules, "parts": parts}

    def is_feasable(self, action, part):
        if not part_fits_in_module(part, self.modules[action]) or self.modules[action].capacity < 0:
            return False
        return True
