import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10, 0.01)

# notice that nrows = number
# of images
plt.subplot(3, 1, 1)
plt.plot(x, np.sin(x))

# ncols stays as 1
plt.subplot(3, 1, 2)
plt.plot(x, np.cos(x))

# each image has a unique
# index
plt.subplot(3, 1, 3)
plt.plot(x, x)

plt.show()
