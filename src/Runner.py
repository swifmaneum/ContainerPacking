from abc import ABCMeta, abstractmethod


class Runner(object):
    @abstractmethod
    def run(self, data):
        raise NotImplementedError
