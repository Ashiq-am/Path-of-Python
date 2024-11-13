import matplotlib.pyplot as plt
import matplotlib.text

fig, ax = plt.subplots()

ax.plot([5,1], label="Label 1")
ax.plot([3,0], label="Label 2")

legend = ax.legend(loc="upper right")

# Create offset from lower right
# corner of legend box, (1.0,0) is
# the coordinates of the offset point
# in the legend coordinate system
offset = matplotlib.text.OffsetFrom(legend, (1.0, 0.0))

# Create annotation. Top right corner
# located -20 pixels below the offset
# point (lower right corner of legend).
ax.annotate("info_string",
			xy = (0,0),
			size = 14,
			xycoords = 'figure fraction',
			xytext = (0,-20),
			textcoords = offset,
			horizontalalignment = 'right',
			verticalalignment = 'top')

# Draw the canvas for offset to take effect
fig.canvas.draw()

plt.show()
