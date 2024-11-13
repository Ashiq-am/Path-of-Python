# Implementation of matplotlib function
from matplotlib.artist import Artist
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

Artist.set_clip_path(im, patch)

fig.suptitle('matplotlib.artist.Artist.set_clip_path()\
function Example', fontweight="bold")

plt.show()
