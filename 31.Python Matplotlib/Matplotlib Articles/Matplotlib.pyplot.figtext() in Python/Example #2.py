# importing required modules
import matplotlib.pyplot as plt
import numpy as np

# values of x and y axes
x = np.arange(0, 8, 0.1)
y = np.sin(x)
plt.plot(x, y)

plt.figtext(0.55, 0.7,
            "Sin curve",
            horizontalalignment="center",
            verticalalignment="center",
            wrap=True, fontsize=14,
            color="green")

plt.xlabel('x')
plt.ylabel('y')
plt.show()
