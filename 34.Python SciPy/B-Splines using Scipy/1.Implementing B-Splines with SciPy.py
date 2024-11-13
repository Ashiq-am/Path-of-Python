import numpy as np
from scipy.interpolate import BSpline
import matplotlib.pyplot as plt

# Define knot vector, coefficients, and degree
t = [0, 1, 2, 3, 4, 5]
c = [-1, 2, 0, -1]
k = 2

# Create a BSpline object
spl = BSpline(t, c, k)

# Evaluate the spline at multiple points
x = np.linspace(1.5, 4.5, 50)
y = spl(x)

plt.plot(x, y)
plt.title('B-Spline Curve')
plt.xlabel('x')
plt.ylabel('S(x)')
plt.grid(True)
plt.show()
