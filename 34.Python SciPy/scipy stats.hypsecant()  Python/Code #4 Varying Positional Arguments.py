import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import hypsecant

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = hypsecant .pdf(x, 1, 3)
y2 = hypsecant .pdf(x, 1, 4)
plt.plot(x, y1, "*", x, y2, "r--")
