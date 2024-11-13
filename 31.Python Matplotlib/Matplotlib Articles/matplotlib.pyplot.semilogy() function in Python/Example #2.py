# importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(nrows = 2,
					ncols = 2,
					figsize =(10, 5))
x = np.random.randn(1000)

# Plot to each different index
ax[0, 0].loglog(x, x / 2)
ax[0, 1].semilogy(np.random.random(10), np.random.random(10))
ax[1, 0].semilogx(np.random.random(10), np.random.random(10))
ax[1, 1].hist(np.random.randn(1000))
