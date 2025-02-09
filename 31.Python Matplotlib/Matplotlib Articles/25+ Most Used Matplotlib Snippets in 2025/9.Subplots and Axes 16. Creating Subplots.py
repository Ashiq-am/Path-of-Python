import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
y2 = np.array([10, 20, 30, 40])

# First plot (1 row and 2 columns)
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Plot 1')

# Second plot (1 row and 2 columns)
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Plot 2')

plt.show()