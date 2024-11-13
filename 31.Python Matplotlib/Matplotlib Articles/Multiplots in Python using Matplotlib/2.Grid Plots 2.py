import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10, 0.01)
plt.subplot(221)
plt.plot(x, np.sin(x))

plt.subplot(222)
plt.plot(x, np.cos(x))

plt.subplot(223)
plt.plot(x, x)

plt.subplot(224)
plt.plot(x, 5-x)
plt.show()
