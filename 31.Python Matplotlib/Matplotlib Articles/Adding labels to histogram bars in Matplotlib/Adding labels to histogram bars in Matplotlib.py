from matplotlib import pyplot as plt
import numpy as np

# Creating dataset
marks = np.array([70, 50, 40, 90, 55, 85, 74, 66, 33, 11, 45, 36, 89])

# Creating histogram
fig, ax = plt.subplots(1, 1)
ax.hist(marks)

# Set title
ax.set_title("Title")

# adding labels
ax.set_xlabel('x-label')
ax.set_ylabel('y-label')

# Make some labels.
rects = ax.patches
labels = ["label%d" % i for i in range(len(rects))]

for rect, label in zip(rects, labels):
	height = rect.get_height()
	ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
			ha='center', va='bottom')

# Show plot
plt.show()
