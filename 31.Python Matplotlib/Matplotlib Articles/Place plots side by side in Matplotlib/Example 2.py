# importing libraries
import numpy as np
import matplotlib.pyplot as plt

# craeting an array of data for x-axis
x = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

# data for y-axis
y_1 = 2*x

# dat for y-axis for another plot
y_2 = 3*x

# using subplot function and creating plot one
# row 2, column 1, count 1
plt.subplot(2, 1, 1)
plt.plot(x, y_1, 'r', linewidth=5, linestyle=':')
plt.title('FIRST PLOT')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# using subplot function and creating plot two
# row 2, column 1, count 2
plt.subplot(2, 1, 2)
plt.plot(x, y_2, 'g', linewidth=5)
plt.title('SECOND PLOT')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# spce between the plots
plt.tight_layout()

# show plot
plt.show()
