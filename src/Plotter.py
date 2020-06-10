import matplotlib.pyplot as plt


class Plotter(object):
    def __init__(self, xs, ys):
        plt.plot(xs, ys)
        plt.xlabel('Anzahl Teile')
        plt.ylabel('Zeit')

    def show(self):
        plt.show()
