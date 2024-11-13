import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.title("Basic Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
