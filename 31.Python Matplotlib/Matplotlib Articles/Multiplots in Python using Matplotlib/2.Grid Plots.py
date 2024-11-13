import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10, 0.01)
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x))

plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x))

plt.subplot(2, 2, 3)
plt.plot(x, x)

plt.subplot(2, 2, 4)
plt.plot(x, 5-x)

plt.show()
