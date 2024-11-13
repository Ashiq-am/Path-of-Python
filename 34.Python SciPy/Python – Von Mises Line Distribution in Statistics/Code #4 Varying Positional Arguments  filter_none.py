import matplotlib.pyplot as plt
import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.optimize.tests.test_lsq_linear import b
from scipy.stats import vonmises_line

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = vonmises_line.pdf(x, a, b)
y2 = vonmises_line.pdf(x, a, b)
plt.plot(x, y1, "*", x, y2, "r--")
