import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = expon.pdf(x, 2, 6)
y2 = expon.pdf(x, 1, 4)
plt.plot(x, y1, "*", x, y2, "r--")
