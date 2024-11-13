from scipy.stats import arcsine
import matplotlib.pyplot as plt
import numpy as np
a = 2
b = 2
x = np.linspace(0, np.minimum(rv.dist.b, 3))

# Varying location and scale
y1 = arcsine.pdf(x, -0.1, .8)
y2 = arcsine.pdf(x, -3.25, 3.25)
plt.plot(x, y1, "*", x, y2, "r--")
