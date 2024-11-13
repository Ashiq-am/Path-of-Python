import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

np.random.seed(10**7)
data = np.random.lognormal(size =(37, 4),
						mean = 4.5,
						sigma = 1.75)
labels = ['G1', 'G2', 'G3', 'G4']

stats = cbook.boxplot_stats(data, labels = labels,
							bootstrap = 100)

for n in range(len(stats)):
	stats[n]['med'] = np.median(data)
	stats[n]['mean'] *= 2

fig, [axes1, axes2, axes3] = plt.subplots(nrows = 1,
										ncols = 3,
										sharey = True)

axes1.bxp(stats)
axes2.bxp(stats, showmeans = True)
axes3.bxp(stats, showmeans = True, meanline = True)

axes2.set_title('matplotlib.axes.Axes.bxp() Example')
plt.show()
