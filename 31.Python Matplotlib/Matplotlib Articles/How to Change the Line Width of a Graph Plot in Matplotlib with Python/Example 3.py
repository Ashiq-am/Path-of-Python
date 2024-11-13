# importing packages
import matplotlib.pyplot as plt
import numpy as np

# create data
x_values = np.linspace(0, 10, 1000)

# Adjust the line widths
for i in range(20):
    plt.plot(x_values, np.sin(x_values) + i * 0.5, lw=i * 0.4)
    plt.plot(x_values, np.cos(x_values) + i * 0.5, lw=i * 0.4)

plt.show()
