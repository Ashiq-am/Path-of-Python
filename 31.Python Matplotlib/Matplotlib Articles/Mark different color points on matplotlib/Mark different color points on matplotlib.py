import numpy as np
import matplotlib.pyplot as plt

# values of x
x = np.array([1, 2, 3, 4, 5,
              6, 7, 8, 9, 10])

# values of y
y = np.array([10, 9, 8, 7, 6, 5,
              4, 3, 2, 1])

# empty list, will hold color value
# corresponding to x
col = []

for i in range(0, len(x)):
    if x[i] < 7:
        col.append('blue')
    else:
        col.append('magenta')

for i in range(len(x)):
    # plotting the corresponding x with y
    # and respective color
    plt.scatter(x[i], y[i], c=col[i], s=10,
                linewidth=0)

plt.show()
