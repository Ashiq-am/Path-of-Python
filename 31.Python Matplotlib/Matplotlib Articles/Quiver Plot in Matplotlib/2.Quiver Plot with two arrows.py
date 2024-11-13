# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# Creating arrow
x_pos = [0, 0]
y_pos = [0, 0]
x_direct = [1, 0]
y_direct = [1, -1]

# Creating plot
fig, ax = plt.subplots(figsize = (12, 7))
ax.quiver(x_pos, y_pos, x_direct, y_direct,
		scale = 5)

ax.axis([-1.5, 1.5, -1.5, 1.5])

# show plot
plt.show()
