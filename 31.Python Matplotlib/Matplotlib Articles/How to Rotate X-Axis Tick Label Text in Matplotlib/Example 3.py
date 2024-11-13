# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating dataset
x = np.arange(0, np.pi*2, 0.05)
y = np.sin(x**2)

# Creating Figure
fig, ax = plt.subplots()

# Creating plot
ax.plot(x, y)

# Rotating X-axis labels
for tick in ax.get_xticklabels():
	tick.set_rotation(75)

# Setting title
plt.title('Rotating using ax.set_xticklabels()')

# Show plot
plt.show()
