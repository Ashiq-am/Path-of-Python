# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams['font.size'] = 8.0

np.random.seed(789680)
data1 = np.random.gamma(4, size =[60, 50])

lineoffsets1 = 1
linelengths1 = 1

fig, [axs1, axs2]= plt.subplots(2, 1)
axs1.eventplot(data1, colors ='green',
			lineoffsets = lineoffsets1,
			linelengths = linelengths1)

axs2.eventplot(data1, colors ='green',
			lineoffsets = lineoffsets1,
			linelengths = linelengths1,
			orientation ='vertical')

axs1.set_title('matplotlib.axes.Axes.eventplot Example')
plt.show()
