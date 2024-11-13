# importing required modules
import matplotlib.pyplot as plt
import numpy as np

# values of x and y axes
x = np.arange(0, 8, 0.1)
y = np.exp(x)
plt.plot(x, y)

# pyplot.figtext(x, y, string)
plt.figtext(0.55, 0.7,
            "Exponential Curve",
            horizontalalignment="center",
            wrap=True, fontsize=10,
            bbox={'facecolor': 'grey',
                  'alpha': 0.3, 'pad': 5})

plt.xlabel('x')
plt.ylabel('y')
plt.show()
