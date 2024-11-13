import numpy as np

# Generate random 3D data points
x = np.random.random(100)
y = np.random.random(100)
z = np.sin(x * y) + np.random.normal(0, 0.1, size=100)
data = np.array([x, y, z]).T
