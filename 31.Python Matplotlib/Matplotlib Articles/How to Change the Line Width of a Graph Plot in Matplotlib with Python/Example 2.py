# importing packages
import matplotlib.pyplot as plt
import numpy as np

# create data
x_values = np.linspace(0, 10, 1000)
y_values = np.sin(x_values)

# Adjust the line widths
for i in range(20):
    plt.plot(x_values, y_values + i * 0.5, lw=i * 0.5)

plt.show()
