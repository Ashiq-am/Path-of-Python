# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating dataset
x = np.arange(0, np.pi*2, 0.05)
y = np.sin(x**2)

# Creating plot
plt.plot(x, y)

# Rotating X-axis labels
plt.xticks(rotation = 25)

# Setting title
plt.title('Rotating using plt.xticks()')

# Show plot
plt.show()
