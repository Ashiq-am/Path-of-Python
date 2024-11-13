# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook

with cbook.get_sample_data('image.PNG') as image_file:
    image = plt.imread(image_file)

fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Rectangle((50, 50), 200, 200,
                          transform=ax.transData)

# use of get_transformed_clip_path_and_affine() method
val = Axis.get_transformed_clip_path_and_affine(im)
ax.set_title("Value Return by get_transformed_clip_path_and_affine(): "
             + str(val))

fig.suptitle("""matplotlib.axis.Axis.get_transformed_clip_path_and_affine() 
function Example\n""", fontweight="bold")

plt.show()
