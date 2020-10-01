import numpy as np
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from keras.models import Sequential
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
from keras.layers import Dense, Activation, Flatten
from pathlib import Path

from Data.ModuleData import ModuleData
from DeepReinforcementLearning.AgentEnvironmentClasses.ProblemGeneratorEnv import ProblemGeneratorEnv
from DeepReinforcementLearning.AgentEnvironmentClasses.TrainingEnv import TrainingEnv
from Helper import Helper
from ProblemGenerators.RandomProblemGenerator import RandomProblemGenerator
from Runner import Runner


class DeepQNetworkRunner(Runner):

    def __init__(self):
        self.environment = TrainingEnv()

        np.random.seed(123)
        self.environment.seed(123)
        nb_actions = self.environment.action_space.n

        self.model = Sequential()
        self.model.add(Flatten(input_shape=(1,) + self.environment.observation_space.shape))
        self.model.add(Dense(64))
        self.model.add(Activation('relu'))
        self.model.add(Dense(64))
        self.model.add(Activation('relu'))
        self.model.add(Dense(64))
        self.model.add(Activation('relu'))
        self.model.add(Dense(nb_actions))
        self.model.add(Activation('linear'))

        memory = SequentialMemory(limit=100000, window_length=1)
        policy = BoltzmannQPolicy()
        self.dqn = DQNAgent(model=self.model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=50,
                            target_model_update=1e-2,
                            policy=policy)
        self.dqn.compile(Adam(lr=1e-3), metrics=['mae'])

        weights = Path('dqn_sorting_weights.h5f.index')
        if not weights.is_file():
            self.train()
        self.dqn.load_weights('dqn_sorting_weights.h5f')

    def train(self):
        self.environment = TrainingEnv()
        self.dqn.fit(self.environment, nb_steps=10000, visualize=False, verbose=2)
        self.dqn.save_weights('dqn_sorting_weights.h5f', overwrite=True)

    def find_solution(self, data):
        self.environment = ProblemGeneratorEnv(data)
        self.dqn.test(self.environment, nb_episodes=1, visualize=False)
        print(self.environment.solution.allocation)
        print(self.environment.solution.wasted_space_sum)
        return self.environment.solution
