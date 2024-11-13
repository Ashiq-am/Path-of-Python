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
ax.set_xticklabels(ax.get_xticks(), rotation = 50)

# Setting title
plt.title('Rotating using tick.set_rotation()')

# Show plot
plt.show()
