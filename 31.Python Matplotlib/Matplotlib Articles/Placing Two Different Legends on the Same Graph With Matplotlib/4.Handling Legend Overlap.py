import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y1, label='Sine')
ax.plot(x, y2, label='Cosine')

# Place legend outside the plot
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Adjust the position of the plot to make room for the legend
# This setting moves the plot leftwards, reducing its width
ax.set_position([0.1, 0.1, 0.6, 0.8])  # [left, bottom, width, height]
plt.show()
