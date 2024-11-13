import matplotlib.pyplot as plt
import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.stats import gengamma

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = gengamma.pdf(x, a, 1, 3)
y2 = gengamma.pdf(x, a, 1, 4)
plt.plot(x, y1, "*", x, y2, "r--")
