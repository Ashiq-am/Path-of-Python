import matplotlib.pyplot as plt
import numpy as np


x = np.array([[0, 1, 2, 3],
			[0, 1, 2, 3],
			[0, 1, 2, 3],
			[0, 1, 2, 3]])

y = np.array([[0.0, 0.0, 0.0, 0],
			[1.0, 1.0, 1.0, 1],
			[2.0, 2.0, 2.0, 2],
			[3, 3, 3, 3]])

values = np.array([[0, 0.5, 1],
				[1, 1.5, 2],
				[2, 2.5, 3]])

fig, ax = plt.subplots()

ax.pcolormesh(x, y, values)
ax.set_aspect('equal')
ax.set_title("pcolormesh_example2")
