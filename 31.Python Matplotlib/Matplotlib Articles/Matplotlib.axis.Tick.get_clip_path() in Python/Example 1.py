# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook


with cbook.get_sample_data('loggf.PNG') as image_file:
	image = plt.imread(image_file)

fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Rectangle((10, 10),
						560,
						500,
						transform=ax.transData)

if Tick.get_clip_path(im) is None:
	im.set_clip_path(patch)

fig.suptitle("""matplotlib.axis.Tick.set_clip_path()
function Example\n""", fontweight="bold")

plt.show()
