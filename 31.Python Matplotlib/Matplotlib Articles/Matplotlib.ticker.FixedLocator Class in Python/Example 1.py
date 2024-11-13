import numpy as np
import matplotlib.pyplot as plt
import matplotlib


np.arange(0, 15, 5)
plt.figure(figsize = [6,4])

x = np.array([1, 2, 3, 4, 5,
			6, 7, 8, 9, 10,
			11, 12, 13, 14, 15])

y = np.array([15, 16, 17, 18,
			19, 20, 40, 50,
			60, 70, 80, 90,
			100, 110, 120])

ax = sns.pointplot(x, y,
				color = 'k',
				markers = ["."],
				scale = 2)

ax.xaxis.set_major_locator(matplotlib.ticker.FixedLocator([1,5,8]))

plt.show()
