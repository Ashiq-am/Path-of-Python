import matplotlib.pyplot as plt
import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.optimize.tests.test_lsq_linear import b
from scipy.stats import weibull_max

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = weibull_max.pdf(x, a, b)
y2 = weibull_max.pdf(x, a, b)
plt.plot(x, y1, "*", x, y2, "r--")
