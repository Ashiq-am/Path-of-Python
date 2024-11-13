# importing libraries
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

fig, ax = plt.subplots()
# Reading image from folder

img = mpimg.imread(r'img.jpg')
image = plt.imshow(img)

# Locating current axes
divider = make_axes_locatable(ax)

# creating new axes on the right
# side of current axes(ax).
# The width of cax will be 5% of ax
# and the padding between cax and ax
# will be fixed at 0.05 inch.
colorbar_axes = divider.append_axes("right",
									size="10%",
									pad=0.1)
# Using new axes for colorbar
plt.colorbar(image, cax=colorbar_axes)
plt.show()
