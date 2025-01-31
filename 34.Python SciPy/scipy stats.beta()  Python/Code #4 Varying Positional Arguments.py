from scipy.stats import arcsine, beta
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1.0, 100)

# Varying positional arguments
y1 = beta.pdf(x, 2.75, 2.75)
y2 = beta.pdf(x, 3.25, 3.25)
plt.plot(x, y1, "*", x, y2, "r--")
