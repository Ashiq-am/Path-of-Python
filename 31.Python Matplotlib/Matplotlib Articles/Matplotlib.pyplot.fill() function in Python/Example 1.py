# Importing the library
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)
plt.plot(x, y)

# Assighning plot attributes
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')

# Filling sign wave curv with cyan color
plt.fill(x, y, "c")
plt.show()
