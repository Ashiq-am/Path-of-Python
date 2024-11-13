import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plotting the data
plt.plot(x, y1, label='Sine Function')
plt.plot(x, y2, label='Cosine Function')

# Adding the legend
plt.legend()
plt.show()
