import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
x = np.arange(0, 10, 0.01)
plt.plot(x, x-5)

plt.title("Not so Tiny")
fig.add_subplot(2, 2, 4)
plt.plot(x, 5-x)

plt.title("Tiny Plot")
plt.show()
