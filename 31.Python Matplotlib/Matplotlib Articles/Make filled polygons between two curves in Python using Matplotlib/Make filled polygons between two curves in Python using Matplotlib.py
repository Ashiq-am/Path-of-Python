import matplotlib.pyplot as plt
import numpy as np
# set the width
width = 3.5

# set the height
height = 2.5

# set the depth
depth = 65

# plot the figure
plt.figure(figsize =(width, height), dpi = depth)

# set the x array of length 3
x = [1, 3, 6]

# set y1 array of length 3
y1 = [2, 3.5, 4]

# set y2 array of length 3
y2 = [3, 4, 5.5]

# fill the horizontal arean between y1 and y2
plt.fill_between(x, y1, y2)

# show the plotted figure
plt.show()
