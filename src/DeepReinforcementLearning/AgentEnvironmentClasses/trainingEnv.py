import gym
import numpy as np
from gym import spaces
from gym.utils import seeding
from AgentClasses.Models.part import Part
from AgentClasses.Models.container import Container
from AgentClasses.AgentEnvironmentClasses.aiRuleBase import get_best_fitting_module


class BoardSortingEnv(gym.Env):

    def __init__(self):
        self.reward = 0
        self.part = ()
        self.np_random = ()
        self.container = Container(90, 600, 2, 320, 600, 2, 890, 600, 2, 1250, 600, 2, 1420, 600, 2, 2000, 600, 2)
        self.next_environment_observation = ()
        self.action_space = spaces.Discrete(7)
        self.observation_space = spaces.Box(low=np.array([40, 40, 0, 0, 0, 0, 0, 0]),
                                            high=np.array([2000, 600, 7, 7, 7, 7, 7, 7]), dtype=np.uint64)
        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)
        self.reward = 0
        self.reward = get_best_fitting_module(action, self.part, self.container.modules)

        self.part = Part(self.np_random, 40, 2000, 40, 600)
        self.container.update_module_capacities(self.np_random)
        self.next_environment_observation = (self.part.length, self.part.width, self.container.modules[0].capacity,
                                             self.container.modules[1].capacity, self.container.modules[2].capacity,
                                             self.container.modules[3].capacity, self.container.modules[4].capacity,
                                             self.container.modules[5].capacity)
        return np.array(self.next_environment_observation), self.reward, True, {}

    def reset(self):
        self.part = Part(self.np_random, 40, 2000, 40, 600)
        self.container.update_module_capacities(self.np_random)
        self.next_environment_observation = (self.part.length, self.part.width, self.container.modules[0].capacity,
                                             self.container.modules[1].capacity, self.container.modules[2].capacity,
                                             self.container.modules[3].capacity, self.container.modules[4].capacity,
                                             self.container.modules[5].capacity)
        return np.array(self.next_environment_observation)
