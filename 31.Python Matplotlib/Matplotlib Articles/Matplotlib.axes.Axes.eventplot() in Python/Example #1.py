#Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams['font.size'] = 8.0

np.random.seed(789680)
data1 = np.random.random([6, 50])

colors1 = ['C{}'.format(i) for i in range(6)]
lineoffsets1 = np.array([-9, -13, 1,
						15, 6, 10])

linelengths1 = [5, 2, 9, 11, 3, 5]

fig, axs = plt.subplots()
axs.eventplot(data1, colors=colors1,
			lineoffsets=lineoffsets1,
			linelengths=linelengths1)

axs.set_title('matplotlib.axes.Axes.eventplot Example')
plt.show()
