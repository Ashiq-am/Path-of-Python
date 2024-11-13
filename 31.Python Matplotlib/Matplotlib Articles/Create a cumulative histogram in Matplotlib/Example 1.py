# importing pyplot for getting graph
import matplotlib.pyplot as plt

# importing numpy for getting array
import numpy as np

# importing scientific python
from scipy import stats

# list of values
x = [10, 40, 20, 10, 30, 10, 56, 45]

res = stats.cumfreq(x, numbins=4,defaultreallimits=(1.5, 5))

# generating random values
rng = np.random.RandomState(seed=12345)

# normalizing
samples = stats.norm.rvs(size=1000,random_state=rng)

res = stats.cumfreq(samples,numbins=25)

x = res.lowerlimit + np.linspace(0, res.binsize*res.cumcount.size,res.cumcount.size)

# specifying figure size
fig = plt.figure(figsize=(10, 4))

# adding sub plots
ax1 = fig.add_subplot(1, 2, 1)

# adding sub plots
ax2 = fig.add_subplot(1, 2, 2)

# getting histogram using hist function
ax1.hist(samples, bins=25,color="green")

# setting up the title
ax1.set_title('Histogram')

# cumulative graph
ax2.bar(x, res.cumcount, width=4, color="blue")

# setting up the title
ax2.set_title('Cumulative histogram')

ax2.set_xlim([x.min(), x.max()])

# display hte figure(histogram)
plt.show()
