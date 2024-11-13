# import Image from wand.image module
from wand.image import Image

# read file using Image function
with Image(filename ="gfg.png") as img:
	# perform adaptive blur effect using adaptive_blur() function
	img.adaptive_blur(radius = 8, sigma = 4)
	# save final image
	img.save(filename ="adblur_gfg.png")
