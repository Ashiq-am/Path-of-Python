# import libraries
import matplotlib.pyplot as plt
import numpy as np

# create image = 10x10 array
img = np.random.randint(-100, 100, (10, 10))

# make plot
fig, ax = plt.subplots()

# show image
shw = ax.imshow(img)

# make bar
bar = plt.colorbar(shw)

# show plot with labels
plt.xlabel('X Label')
plt.ylabel('Y Label')
bar.set_label('ColorBar')
plt.show()
