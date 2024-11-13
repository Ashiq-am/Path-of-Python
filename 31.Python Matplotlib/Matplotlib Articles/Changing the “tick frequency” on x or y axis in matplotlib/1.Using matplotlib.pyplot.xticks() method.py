import matplotlib.pyplot as plt
import numpy as np
x = [20, 70, 105, 220, 385, 590, 859]
y = [10, 20, 30, 40, 50, 60, 70]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xticks(np.arange(0, 1000, 100))
plt.show()
