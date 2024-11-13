# importing all important libraries
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np

# plotting the graph
fig, ax = plt.subplots()

x = np.linspace(0, 10, 20)
y = np.cos(x)
ax.set_title('Cosine Values', fontsize=15)
ax.set_xlabel('Value')
ax.set_ylabel('Cosine')

# reading the image
image = plt.imread('emoji.png')

# OffsetBox
image_box = OffsetImage(image, zoom=0.1)

# creating annotation for each point
# on the graph
x, y = np.atleast_1d(x, y)

# for each value of (x,y), we create
# an annotation
for x0, y0 in zip(x, y):
	ab = AnnotationBbox(image_box, (x0, y0), frameon=False)
	ax.add_artist(ab)

ax.plot(x,y, c='green')
plt.show()
