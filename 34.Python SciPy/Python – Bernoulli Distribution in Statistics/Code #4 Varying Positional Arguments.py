import matplotlib.pyplot as plt
import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.optimize.tests.test_lsq_linear import b
from scipy.stats import bernoulli

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = bernoulli.ppf(x, a, b)
y2 = bernoulli.pmf(x, a, b)
plt.plot(x, y1, "*", x, y2, "r--")
