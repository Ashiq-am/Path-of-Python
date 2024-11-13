# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook

# image used is
# https://media.geeksforgeeks.org/
# wp-content/uploads/20200402214740/geek.jpg
with cbook.get_sample_data('geek.jpg') as image_file:
    image = plt.imread(image_file)

fig, ax = plt.subplots()
im = ax.imshow(image)

patch = patches.Rectangle((0, 0), 260, 200,
                          transform=ax.transData)
im.set_clip_path(patch)

print("List of the child Artists of this Artist \n",
      *list(ax.get_images()), sep="\n")

fig.suptitle('matplotlib.axes.Axes.get_images() \
function Example', fontweight="bold")

plt.show()
