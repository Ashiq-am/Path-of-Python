import matplotlib.pyplot as plt
import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.sparse.linalg.isolve.tests.test_gcrotmk import b
from scipy.stats import geom

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = geom.ppf(x, a, b)
y2 = geom.pmf(x, a, b)
plt.plot(x, y1, "*", x, y2, "r--")
