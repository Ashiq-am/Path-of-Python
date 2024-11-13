# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(9680801)

mu, sigma = 50, 13
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50,
							density = True,
							facecolor ='g',
							alpha = 0.75)


plt.xlabel('No of Users in K')
plt.title('Histogram of IQ')
plt.text(50, .035, r'$\mu = 50,\ \ \sigma = 13$')

plt.xlim(-10, 110)
plt.ylim(0, 0.04)

plt.grid(True)
plt.title(" matplotlib.pyplot.ylim() Example")

plt.show()
