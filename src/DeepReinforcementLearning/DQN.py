'''
look at minizincmodelrunner structure for dqn class

'''

import datetime
import numpy as np
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from keras.models import Sequential
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
from keras.layers import Dense, Activation, Flatten

from Data.ModuleData import ModuleData
from DeepReinforcementLearning.AgentEnvironmentClasses.ProblemGeneratorEnv import ProblemGeneratorEnv
from DeepReinforcementLearning.AgentEnvironmentClasses.env import env
from DeepReinforcementLearning.AgentEnvironmentClasses.trainingEnv import BoardSortingEnv
from Helper import Helper
from ProblemGenerators.RandomProblemGenerator import RandomProblemGenerator

# TODO: Remove glue code if not needed any more
# Begin glue code
problem_generator = RandomProblemGenerator(1)
parts = []

for i in range(1, 20):
    parts = parts + next(problem_generator)

min_number_of_containers = Helper.find_min_number_of_containers(parts, ModuleData.get_container_modules(), 1)
modules = ModuleData.get_container_modules(min_number_of_containers)
data = {"modules": modules, "parts": parts}
# End glue code

enable_training = 0
if enable_training == 1:
    environment = ProblemGeneratorEnv(data)
else:
    environment = ProblemGeneratorEnv(data)
np.random.seed(123)
environment.seed(123)
nb_actions = environment.action_space.n

model = Sequential()
model.add(Flatten(input_shape=(1,) + environment.observation_space.shape))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
print(model.summary())

memory = SequentialMemory(limit=100000, window_length=1)
policy = BoltzmannQPolicy()
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=50, target_model_update=1e-2,
               policy=policy)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

if enable_training == 1:
    dqn.fit(environment, nb_steps=100000, visualize=False, verbose=2)
    dqn.save_weights('dqn_sorting_weights.h5f', overwrite=True)
else:
    dqn.load_weights('dqn_sorting_weights.h5f')
    start_time = datetime.datetime.now()
    dqn.test(environment, nb_episodes=15, visualize=False)
    end_time = datetime.datetime.now()
