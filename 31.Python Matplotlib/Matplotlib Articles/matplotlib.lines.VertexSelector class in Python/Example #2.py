import matplotlib.pyplot as plt
import matplotlib.lines as lines
from matplotlib.collections import PathCollection

lines.VertexSelector


# class for plot clicked area
class dragged_lines:

    # constructor for the dragged_lines class
    def __init__(self, ax):
        self.ax = ax
        self.c = ax.get_figure().canvas

        self.line = lines.Line2D(x, y, picker=5, marker='o',
                                 markerfacecolor='g', color='y')

        self.ax.add_line(self.line)
        self.c.draw_idle()
        self.sid = self.c.mpl_connect('pick_event', self.lineclicker)

    def lineclicker(self, event):
        if event.artist:
            print("line selected ", event.artist)
            self.follower = self.c.mpl_connect("motion_notify_event",
                                               self.mouse_follower)
            self.releaser = self.c.mpl_connect("button_press_event",
                                               self.release_after_click)

    def mouse_follower(self, event):
        self.line.set_data([event.xdata, event.ydata])
        self.c.draw_idle()

    def release_after_click(self, event):
        data = self.line.get_data()
        print(data)

        self.c.mpl_disconnect(self.releaser)
        self.c.mpl_disconnect(self.follower)


figure = plt.figure()
axes = figure.add_subplot(111)
x_axis, y_axis = [2, 4, 5, 7], [8, 6, 12, 9]
axes.plot(x_axis, y_axis)
Vline = dragged_lines(axes)
plt.show()
