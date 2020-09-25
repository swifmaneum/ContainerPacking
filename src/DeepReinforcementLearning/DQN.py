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
from DeepReinforcementLearning.AgentEnvironmentClasses.env import env
from DeepReinforcementLearning.AgentEnvironmentClasses.trainingEnv import BoardSortingEnv


enable_training = 1
if enable_training == 1:
    environment = BoardSortingEnv()
else:
    environment = env(60, 400, 0, 0, 0, 0, 0, 0)
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
