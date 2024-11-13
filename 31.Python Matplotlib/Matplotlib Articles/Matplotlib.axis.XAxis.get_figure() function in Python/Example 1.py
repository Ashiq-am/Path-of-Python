# Implementation of matplotlib function
from matplotlib.axis import XAxis
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.transforms as mtransforms
import matplotlib.text as mtext


class GFGfun(lines.Line2D):

    def __init__(self, *args, **kwargs):
        self.text = mtext.Text(0, 0, '')
        lines.Line2D.__init__(self, *args, **kwargs)
        self.text.set_text(self.get_label())

    def set_figure(self, figure):
        self.text.set_figure(figure)
        lines.Line2D.set_figure(self, figure)

    def set_axes(self, axes):
        self.text.set_axes(axes)
        lines.Line2D.set_axes(self, axes)

    def set_transform(self, transform):
        # 2 pixel offset
        texttrans = transform + mtransforms.Affine2D().translate(3, 3)
        self.text.set_transform(texttrans)
        lines.Line2D.set_transform(self, transform)

    def set_data(self, x, y):
        if len(x):
            self.text.set_position((x[-1], y[-1]))

        lines.Line2D.set_data(self, x, y)

    def draw(self, renderer):
        lines.Line2D.draw(self, renderer)
        self.text.draw(renderer)


np.random.seed(10 ** 7)

fig, ax = plt.subplots()
x, y = np.random.rand(2, 30)
line = GFGfun(x, y, mfc='green',
              ms=12,
              label='Label')

line.text.set_color('green')
line.text.set_fontsize(16)

ax.add_line(line)

ax.text(0.4, 0.7, "Value Return : "
        + str(XAxis.get_figure(ax)),
        fontweight="bold")

fig.suptitle("""matplotlib.axis.XAxis.get_figure() 
function Example\n""", fontweight="bold")

plt.show()
