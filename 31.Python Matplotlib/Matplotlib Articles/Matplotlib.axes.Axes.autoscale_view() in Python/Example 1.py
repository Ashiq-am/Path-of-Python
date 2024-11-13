# ImpleIn Reviewtation of matplotlib function
import numpy as np
from basic_units import cm, inch
import matplotlib.pyplot as plt


N = 5
val1 = [150 * cm, 160 * cm, 146 * cm,
		172 * cm, 155 * cm]

val2 = [20 * cm, 30 * cm, 32 * cm,
		10 * cm, 20 * cm]

fig, ax = plt.subplots()

ind = np.arange(N)
width = 0.35
ax.bar(ind, val1, width, bottom = 0 * cm,
	yerr = val2, label ='In Review')

woval1 = (145 * cm, 149 * cm, 172 * cm,
		165 * cm, 200 * cm)
woval2 = (30 * cm, 25 * cm, 20 * cm,
		31 * cm, 22 * cm)
ax.bar(ind + width, woval1, width,
	bottom = 0 * cm, yerr = woval2,
	label ='Published')

ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Geek1', 'Geek2',
					'Geek3', 'Geek4',
					'Geek5'))

ax.legend()
ax.set_ylabel("Articles")
ax.autoscale_view()

fig.suptitle('matplotlib.axes.Axes.autoscale_view() function Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
