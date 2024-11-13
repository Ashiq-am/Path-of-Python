import matplotlib.pyplot as plt
import numpy as np


# Define X and Y variable data
x = np.array([1, 2, 3, 4])
y = x*2

plt.plot(x, y)
plt.xlabel("X-axis") # add X-axis label
plt.ylabel("Y-axis") # add Y-axis label
plt.title("Any suitable title") # add title
plt.show()
