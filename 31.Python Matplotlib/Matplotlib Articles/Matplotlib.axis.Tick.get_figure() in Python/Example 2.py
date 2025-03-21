# Implementation of matplotlib function
from matplotlib.axis import Tick
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


np.random.seed(10**7)


fig, ax = plt.subplots()
x, y = np.random.rand(2, 10)
line = GFGfun(x, y,
			mfc='green', ms=12, label='Label')

line.text.set_color('green')
line.text.set_fontsize(16)

ax.add_line(line)

ax.text(0.2, 0.8, "Value Return : "
		+ str(Tick.get_figure(ax)),
		fontweight="bold")

fig.suptitle("""matplotlib.axis.Tick.get_figure()
function Example\n""", fontweight="bold")

plt.show()
