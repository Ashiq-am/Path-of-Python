# import modules
import numpy as np
import matplotlib.pyplot as plt

# mean and standard deviation
mu, sigma = 3., 1.
s = np.random.lognormal(mu, sigma, 10000)

# depict illustration
count, bins, ignored = plt.hist(s, 30,
								density=True,
								color='green')
x = np.linspace(min(bins),
				max(bins), 10000)

pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
	/ (x * sigma * np.sqrt(2 * np.pi)))

# assign other attributes
plt.plot(x, pdf, color='black')
plt.grid()
plt.show()
