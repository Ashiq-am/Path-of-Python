# import required modules
import matplotlib.pyplot as plt
import numpy as np

# assign coordinates
x = np.arange(1, 6)
y1 = x**2
y2 = x**4

# depict illustration
plt.scatter(x, y1, label="x**2")
plt.scatter(x, y2, label="x**4")

# apply legend()
plt.legend()
plt.show()
