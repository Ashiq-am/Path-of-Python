import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
sizes = np.random.rand(100) * 100
colors = np.random.rand(100)

plt.scatter(x, y, s=sizes, c=colors)
plt.show()
