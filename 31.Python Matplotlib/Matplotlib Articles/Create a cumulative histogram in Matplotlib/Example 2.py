# importing numpy for getting array
import numpy as np

# importing scientific python
from scipy import stats

# list of values
x = [10, 40, 20, 10, 30, 10, 56, 45]

res = stats.cumfreq(x, numbins=4,
					defaultreallimits=(1.5, 5))

# generating random values
rng = np.random.RandomState(seed=12345)

# normalizing
samples = stats.norm.rvs(size=1000,
						random_state=rng)

res = stats.cumfreq(samples,
					numbins=25)

x = res.lowerlimit + np.linspace(0, res.binsize*res.cumcount.size,
								res.cumcount.size)

fig = plt.figure(figsize=(10, 4))

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.hist(samples, bins=25, color="green")

ax1.set_title('Histogram')
ax2.bar(x, x, width=2, color="blue")

ax2.set_title('Cumulative histogram')
ax2.set_xlim([x.min(), x.max()])

plt.show()
