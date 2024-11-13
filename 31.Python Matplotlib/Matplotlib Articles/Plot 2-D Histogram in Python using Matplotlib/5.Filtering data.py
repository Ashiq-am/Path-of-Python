# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import random

# Creating dataset
x = np.random.normal(size = 500000)
y = x * 3 + 4 * np.random.normal(size = 500000)

# Creating bins
x_min = np.min(x)
x_max = np.max(x)

y_min = np.min(y)
y_max = np.max(y)

x_bins = np.linspace(x_min, x_max, 50)
y_bins = np.linspace(y_min, y_max, 20)

# Creating data filter
data = np.c_[x, y]

for i in range(10000):
	x_idx = random.randint(0, 500000)
	data[x_idx, 0] = -9999

data = data[data[:, 0]!=-9999]

fig, ax = plt.subplots(figsize =(10, 7))
# Creating plot
plt.hist2d(data[:, 0], data[:, 1], bins =[x_bins, y_bins])
plt.title("Filtering data")

ax.set_xlabel('X-axis')
ax.set_ylabel('X-axis')

# show plot
plt.tight_layout()
plt.plot.show()
