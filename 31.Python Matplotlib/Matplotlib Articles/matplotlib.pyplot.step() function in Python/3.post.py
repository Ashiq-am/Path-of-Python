import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 4, 5, 7])
y = np.array([1, 9, 16, 25, 49])

plt.step(x, y, 'r*', where='post')
plt.show()
