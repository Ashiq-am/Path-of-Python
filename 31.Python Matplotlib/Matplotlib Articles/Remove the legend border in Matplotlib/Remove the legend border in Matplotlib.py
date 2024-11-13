# impoting packages
import numpy as np
import matplotlib.pyplot as plt

# create data
x = np.linspace(1, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

# plot graph
plt.plot(x, y1)
plt.plot(x, y2)

# add legend
plt.legend(['Sine wave', 'Cos wave'])
plt.show()
