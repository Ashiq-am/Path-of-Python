# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook

with cbook.get_sample_data('image.PNG') as image_file:
    image = plt.imread(image_file)

fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Rectangle((10, 10), 100, 100,
                          transform=ax.transData)

val = Tick.get_transformed_clip_path_and_affine(im)
ax.set_title("Value Return by get_transformed_clip_path_and_affine(): "
             + str(val))

fig.suptitle("""matplotlib.axis.Tick.get_transformed_clip_path_and_affine()\n
function Example\n""", fontweight="bold")

plt.show()
