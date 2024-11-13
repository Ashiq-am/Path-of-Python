import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gausshyper

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = gausshyper .pdf(x, a, z, 1, 3)
y2 = gausshyper .pdf(x, a, z, 1, 4)
plt.plot(x, y1, "*", x, y2, "r--")
