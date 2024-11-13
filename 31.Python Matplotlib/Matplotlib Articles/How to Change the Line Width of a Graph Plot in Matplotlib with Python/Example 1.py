# importing packages
import matplotlib.pyplot as plt
import numpy as np

# create data
x_values = np.arange(0, 10)
y_values = np.arange(0, 10)

# Adjust the line widths
plt.plot(x_values, y_values - 2, linewidth=5)
plt.plot(x_values, y_values)
plt.plot(x_values, y_values + 2, lw=5)

# add legends and show
plt.legend(['Lw = 5', 'Lw = auto', 'Lw = 5'])
plt.show()
