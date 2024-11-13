import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines


# class for highlighting selected area
class Highlighter(lines.VertexSelector):

    # constructor for the highlighter class
    def __init__(self, line, fmt='ro', **kwargs):
        lines.VertexSelector.__init__(self, line)
        self.markers, = self.axes.plot([], [], fmt, **kwargs)

    # helper function process selected area and plot graph accordingly
    def process_selected(self, ind, xs, ys):
        self.markers.set_data(xs, ys)
        self.canvas.draw()


figure, ax = plt.subplots()
x_axis, y_axis = np.random.rand(2, 30)
line, = ax.plot(x_axis, y_axis, 'bs-', picker=5)

selector = Highlighter(line)
plt.show()
