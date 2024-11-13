# importing required modules
import matplotlib.pyplot as plt
import numpy as np

# values of x and y axes
x = np.arange(0, 8, 0.1)
y = np.sin(x)
plt.plot(x, y)

# pyplot.figtext(x, y, string)
plt.figtext(0, 0, "This is a sample example \
explaining figtext", fontsize=10)

plt.xlabel('x')
plt.ylabel('y')
plt.show()
