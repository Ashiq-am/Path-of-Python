import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
sizes = np.random.rand(100) * 100

plt.scatter(x, y, s=sizes * 10)
plt.show()
