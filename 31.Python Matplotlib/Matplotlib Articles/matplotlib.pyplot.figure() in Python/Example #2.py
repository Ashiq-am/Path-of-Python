# Implementation of matplotlib function
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig = plt.figure(figsize =(4, 4))

ax = Subplot(fig, 111)
fig.add_subplot(ax)

ax.axis["left"].set_visible(False)
ax.axis["bottom"].set_visible(False)

plt.title('matplotlib.pyplot.figure() Example\n',
				fontsize = 14, fontweight ='bold')

plt.show()
