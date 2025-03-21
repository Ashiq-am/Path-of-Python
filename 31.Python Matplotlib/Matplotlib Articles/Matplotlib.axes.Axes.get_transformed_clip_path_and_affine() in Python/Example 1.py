# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook

with cbook.get_sample_data('loggf.PNG') as image_file:
    image = plt.imread(image_file)

fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Rectangle((0, 0), 260, 200,
                          transform=ax.transData)

ax.set_title("Value Return by get_transformed_clip_path_and_affine(): "
             + str(im.get_transformed_clip_path_and_affine()))

fig.suptitle('matplotlib.axes.Axes.get_transformed_clip_path_and_affine()\
function Example\n\n', fontweight="bold")

plt.show()
