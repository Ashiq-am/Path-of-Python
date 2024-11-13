# importing libraries
import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.array([-2, -1, 0, 1, 2])
y1 = x*0
y2 = x*x
y3 = -x*x

# plot the graph
plt.plot(x, y2, alpha=0.2)
plt.plot(x, y1, alpha=0.5)
plt.plot(x, y3, alpha=1)
plt.legend(["op = 0.2", "op = 0.5", "op = 1"])
plt.show()
