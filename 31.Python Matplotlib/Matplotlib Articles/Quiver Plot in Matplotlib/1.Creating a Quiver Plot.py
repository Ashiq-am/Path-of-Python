# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# Creating arrow
x_pos = 0
y_pos = 0
x_direct = 1
y_direct = 1

# Creating plot
fig, ax = plt.subplots(figsize = (12, 7))
ax.quiver(x_pos, y_pos, x_direct, y_direct)
ax.set_title('Quiver plot with one arrow')

# Show plot
plt.show()
