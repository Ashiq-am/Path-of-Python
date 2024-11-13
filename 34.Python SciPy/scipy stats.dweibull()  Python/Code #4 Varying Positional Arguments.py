import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import dweibull

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = dweibull.pdf(x, 1, 6)
y2 = dweibull.pdf(x, 1, 5)
plt.plot(x, y1, "*", x, y2, "r--")
