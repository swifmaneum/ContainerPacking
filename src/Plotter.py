import matplotlib.pyplot as plt


class Plotter(object):
    def __init__(self):
        plt.xlabel('Anzahl Teile')
        plt.ylabel('Zeit in Sekunden')
        plt.grid()

    def add_line(self, xs, ys, label):
        plt.plot(xs, ys, label=label)

    def show(self):
        plt.legend(loc="lower right")
        plt.show()
