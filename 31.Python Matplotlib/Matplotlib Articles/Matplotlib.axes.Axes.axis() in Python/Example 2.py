# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook

# image used is
# https://media.geeksforgeeks.org / wp-content
# / uploads / 20200402214740 / geek.jpg
with cbook.get_sample_data('geek.JPG') as image_file:
	image = plt.imread(image_file)

fig, (ax, ax1) = plt.subplots(2, 1)
im = ax.imshow(image)
patch = patches.Rectangle((0, 0), 260, 200,
						transform = ax.transData)
im.set_clip_path(patch)
ax.set_title('Without Axis Function',
			fontsize = 10, fontweight ='bold')

im = ax1.imshow(image)
patch = patches.Rectangle((0, 0), 260, 200,
						transform = ax1.transData)
im.set_clip_path(patch)
ax1.axis('off')

ax1.set_title("Axis Function with 'Off' option",
			fontsize = 10, fontweight ='bold')
plt.show()
