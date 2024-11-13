# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook

with cbook.get_sample_data('image.PNG') as image_file:
    image = plt.imread(image_file)

fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Rectangle((0, 0), 260, 200,
                          transform=ax.transData)

# use of get_transformed_clip_path_and_affine() method
val = Artist.get_transformed_clip_path_and_affine(im)
ax.set_title("Value Return by get_transformed_clip_path_and_affine(): "
             + str(val))

fig.suptitle('matplotlib.artist.Artist.get_transformed_clip_path_and_affine() \
function Example', fontweight="bold")

plt.show()
