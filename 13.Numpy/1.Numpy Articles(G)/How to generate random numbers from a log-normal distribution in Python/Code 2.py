# Importing required modules
import numpy as np
import matplotlib.pyplot as plt

b = []

# Generating 1000 points from normal distribution.
for i in range(1000):
	a = 12. + np.random.standard_normal(100)
	b.append(np.product(a))

# Making all negative values into positives
b = np.array(b) / np.min(b)
count, bins, ignored = plt.hist(b, 100,
								density=True,
								color='green')

sigma = np.std(np.log(b))
mu = np.mean(np.log(b))

# Plotting the graph.
x = np.linspace(min(bins), max(bins), 10000)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
	/ (x * sigma * np.sqrt(2 * np.pi)))

plt.plot(x, pdf,color='black')
plt.grid()
plt.show()
