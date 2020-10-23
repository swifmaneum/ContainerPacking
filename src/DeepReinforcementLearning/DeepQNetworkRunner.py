import numpy as np
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from keras.models import Sequential
from rl.policy import BoltzmannQPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory
from keras.layers import Dense, Activation, Flatten
from pathlib import Path

from Data.ModuleData import ModuleData
from DeepReinforcementLearning.AgentEnvironmentClasses.ProblemGeneratorEnv import ProblemGeneratorEnv
from DeepReinforcementLearning.AgentEnvironmentClasses.TrainingEnv import TrainingEnv
from DeepReinforcementLearning.AgentEnvironmentClasses.aiRuleBase import part_fits_in_module
from Helper import Helper
from ProblemGenerators.RandomProblemGenerator import RandomProblemGenerator
from Runner import Runner


class DeepQNetworkRunner(Runner):

    def __init__(self):
        self.environment = TrainingEnv()

        np.random.seed(1)
        self.environment.seed(1)
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

        memory = SequentialMemory(limit=10000, window_length=1)
        policy = BoltzmannQPolicy()
        'Compare diffrent configurations'
        self.dqn = DQNAgent(model=self.model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=100,
                            target_model_update=1e-2, enable_dueling_network=True, dueling_type='avg',
                            enable_double_dqn=True, policy=policy, gamma=0.0)
        self.dqn.compile(Adam(lr=1e-3), metrics=['mae'])

        weights = Path('dqn_sorting_weights.h5f.index')
        if not weights.is_file():
            self.train()
        self.dqn.load_weights('dqn_sorting_weights.h5f')

    def train(self):
        self.environment = TrainingEnv()
<<<<<<< HEAD
        steps = 1000000
=======
        steps = 40000
>>>>>>> parent of 079cfaa... Training with 500.000 Steps
        window_size = 100
        points_to_plot = []

        history = self.dqn.fit(self.environment, nb_steps=steps, visualize=False, verbose=2)
        for i in range(0, steps):
            points_to_plot.append(np.mean(history.history['episode_reward'][i * window_size:(i + 1) * window_size]))
        from matplotlib import pyplot as plt
        plt.plot(points_to_plot)
        plt.title('avg reward over time')
        plt.ylabel('average reward')
        plt.xlabel('epoch')
        plt.show()
        self.dqn.save_weights('dqn_sorting_weights.h5f', overwrite=True)

    def find_solution(self, data):
        self.environment = ProblemGeneratorEnv(data)
        self.dqn.test(self.environment, nb_episodes=1, visualize=False)
        if self.is_feasable(self.environment.solution):
            return self.environment.solution
        else:
            return None

    def is_feasable(self, solution):
        for i in range(len(solution.allocation)):
            part = self.environment.parts[i]
            module = self.environment.modules[solution.allocation[i]]
            if not part_fits_in_module(part, module):
                return False
        return True
