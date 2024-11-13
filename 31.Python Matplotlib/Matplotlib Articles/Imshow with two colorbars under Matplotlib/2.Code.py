# import libraries
import matplotlib.pyplot as plt
import numpy as np
from numpy.ma import masked_array

# create image = 10x10 array
img = np.random.randint(-100, 100, (10, 10))

# masked array to positive and negative values
neg_img = masked_array(img, img >= 0)
pos_img = masked_array(img, img < 0)

# make plot
fig, ax = plt.subplots()

# show image
shw1 = ax.imshow(neg_img, cmap=plt.cm.Reds)
shw2 = ax.imshow(pos_img, cmap=plt.cm.winter)

# make bars
bar1 = plt.colorbar(shw1)
bar2 = plt.colorbar(shw2)

# show plot with labels
plt.xlabel('X Label')
plt.ylabel('Y Label')
bar1.set_label('ColorBar 1')
bar2.set_label('ColorBar 2')
plt.show()
