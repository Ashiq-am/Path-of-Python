# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.lines as lines


fig = plt.figure()
fig.add_artist(lines.Line2D([0, 1, 0.5], [0, 1, 0.3]))
fig.add_artist(lines.Line2D([0, 1, 0.5], [1, 0, 0.2]))

plt.title('matplotlib.pyplot.figure() Example\n',
				fontsize = 14, fontweight ='bold')

plt.show()
