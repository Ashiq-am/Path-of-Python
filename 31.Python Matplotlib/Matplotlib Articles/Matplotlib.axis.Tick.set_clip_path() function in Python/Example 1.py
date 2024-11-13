# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook

with cbook.get_sample_data('geeksforgeeks-logo1.PNG') as image_file:
    image = plt.imread(image_file)

fig, ax = plt.subplots()
ax.imshow(image)
patch = patches.Rectangle((10, 10),
                          560,
                          500,
                          transform=ax.transData)

ax.set_clip_path(patch)

fig.suptitle('matplotlib.axis.Tick.set_clip_path() \
function Example', fontweight="bold")

plt.show()
