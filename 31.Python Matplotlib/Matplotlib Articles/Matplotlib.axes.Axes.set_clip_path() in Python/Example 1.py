# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook


with cbook.get_sample_data('loggf.PNG') as image_file:
	image = plt.imread(image_file)

fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Rectangle((0, 0),
						260,
						200,
						transform = ax.transData)
im.set_clip_path(patch)

fig.suptitle('matplotlib.axes.Axes.set_clip_path() function Example\n\n', fontweight ="bold")

plt.show()
