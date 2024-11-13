import numpy as np
import matplotlib.pyplot as plt

np.random.seed(21)
data = np.random.random(111)
quartile1, median, quartile3 = np.percentile(data,
											[ 50, 75,100],
											axis=0)
plt.violinplot(data)
plt.vlines(1, quartile1,
		quartile3,
		color='r',
		linestyle='--')

plt.hlines(quartile1,.7,1.2)
plt.hlines(quartile3,.7,1.2)
