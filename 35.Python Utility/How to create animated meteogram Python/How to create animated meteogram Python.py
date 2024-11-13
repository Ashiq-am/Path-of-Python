# Import imageio packages
# Generate GIF/animation of meteogram
import imageio
from pathlib import Path


image_path = Path('../input/meteogram')
images = list(image_path.glob('*.png'))

# create an array to
# store meteogram images
image_list = []
for file_name in images:
	image_list.append(imageio.imread(file_name))

# to verify all images are read
image_list

# using this function will write images to a
# specified file animated_meteogram.gif
imageio.mimwrite('animated_meteogram.gif', image_list)
