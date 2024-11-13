# Import the required libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline

x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)
plt.title("Univariate Spline")
plt.plot(x, y, 'g.', ms=8)

# Using the default values for the
# smoothing parameter
spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'green', lw=3)

# Manually change the amount of smoothing
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), color='black', lw=3)
plt.show()
