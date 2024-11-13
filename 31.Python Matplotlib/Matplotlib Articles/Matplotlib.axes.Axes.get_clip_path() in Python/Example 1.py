# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook

with cbook.get_sample_data('geek.jpg') as image_file:
    image = plt.imread(image_file)

fig, ax = plt.subplots()
im = ax.imshow(image)

patch = patches.Rectangle((0, 0),
                          260,
                          200,
                          transform=ax.transData)

if im.get_clip_path() is None:
    im.set_clip_path(patch)

fig.suptitle('matplotlib.axes.Axes.get_clip_path() \
function Example\n\n', fontweight="bold")

plt.show()
