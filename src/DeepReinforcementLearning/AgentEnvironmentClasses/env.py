import gym
import numpy as np
from gym import spaces
from gym.utils import seeding
from AgentClasses.Models.part import Part
from AgentClasses.Models.container import Container
from AgentClasses.AgentEnvironmentClasses.aiRuleBase import get_best_fitting_module


class env(gym.Env,):

    def __init__(self, length, width, cap0, cap1, cap2, cap3, cap4, cap5):
        self.part = ()
        self.length = length
        self.width = width
        self.container = Container(90, 600, 2, 320, 600, 2, 890, 600, 2, 1250, 600, 2, 1450, 600, 2, 2000, 600, 2)
        self.container.modules[0].capacity = cap0
        self.container.modules[1].capacity = cap1
        self.container.modules[2].capacity = cap2
        self.container.modules[3].capacity = cap3
        self.container.modules[4].capacity = cap4
        self.container.modules[5].capacity = cap5
        self.reward = 0
        self.next_environment_observation = ()
        self.action_space = spaces.Discrete(7)
        self.observation_space = spaces.Box(low=np.array([40, 40, 0, 0, 0, 0, 0, 0]),
                                            high=np.array([2000, 600, 3, 3, 3, 3, 3, 3]), dtype=np.uint64)
        self.np_random = ()
        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)
        print(action)
        self.part = Part(self.np_random, 20, 2000, 40, 600)
        self.part.length = self.length
        self.part.width = self.width
        self.reward = 0
        self.reward = get_best_fitting_module(action, self.part, self.container.modules)

        self.next_environment_observation = (self.part.length, self.part.width, self.container.modules[0].capacity,
                                             self.container.modules[1].capacity, self.container.modules[2].capacity,
                                             self.container.modules[3].capacity, self.container.modules[4].capacity,
                                             self.container.modules[5].capacity)
        return np.array(self.next_environment_observation), self.reward, True, {}

    def reset(self):
        self.part = Part(self.np_random, 40, 2000, 40, 600)
        self.part.length = self.length
        self.part.width = self.width
        self.next_environment_observation = (self.part.length, self.part.width, self.container.modules[0].capacity,
                                             self.container.modules[1].capacity, self.container.modules[2].capacity,
                                             self.container.modules[3].capacity, self.container.modules[4].capacity,
                                             self.container.modules[5].capacity)
        return np.array(self.next_environment_observation)