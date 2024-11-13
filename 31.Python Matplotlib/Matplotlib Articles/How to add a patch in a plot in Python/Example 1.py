# import modules
import numpy as np
import matplotlib.pyplot as plt

# adjust figure and assign coordinates
y, x = np.mgrid[:5, 1:6]
poly_coords = [(25, 75), (25, 75), (25, 75), (25, 75)]
fig, ax = plt.subplots()

# depict illustration
cells = ax.plot(x, y, x + y)
ax.add_patch(plt.Polygon(poly_coords))

plt.show()
