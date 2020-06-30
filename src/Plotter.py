import matplotlib.pyplot as plt


class Plotter(object):

    def add_figure(self, title, x_label, y_label):
        figure = plt.figure()
        plt.grid()
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        return figure.number

    def add_line(self, data, label, figure_number):
        """ Add a list of tuples (x, y) as a line plot, see https://stackoverflow.com/a/18458953/5730444"""
        plt.figure(figure_number)
        plt.plot(*zip(*data), label=label)

        plt.legend(loc="lower right")

    def show(self):
        plt.show()
