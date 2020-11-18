import numpy as np
from rl.policy import Policy


class DecreasingEpsGreedyQPolicy(Policy):
    """Implement the epsilon greedy policy

    Eps Greedy policy either:

    - takes a random action with probability epsilon
    - takes current best action with prob (1 - epsilon)
    """

    def __init__(self, eps=.1, min_eps=.01, eps_decay=.000001):
        super(DecreasingEpsGreedyQPolicy, self).__init__()
        self.eps_decay = eps_decay
        self.min_eps = min_eps
        self.eps = eps
        self.counter = 0

    def select_action(self, q_values):
        """Return the selected action

        # Arguments
            q_values (np.ndarray): List of the estimations of Q for each action

        # Returns
            Selection action
        """
        assert q_values.ndim == 1
        nb_actions = q_values.shape[0]

        if np.random.uniform() < self.eps:
            action = np.random.randint(0, nb_actions)
        else:
            action = np.argmax(q_values)

        if self.eps > self.min_eps:
            self.eps -= self.eps_decay
        return action

    def get_config(self):
        """Return configurations of EpsGreedyQPolicy

        # Returns
            Dict of config
        """
        config = super(DecreasingEpsGreedyQPolicy, self).get_config()
        config['eps'] = self.eps
        return config
