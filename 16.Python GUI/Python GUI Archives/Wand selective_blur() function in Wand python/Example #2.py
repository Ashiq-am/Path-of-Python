# import display() to show final image
from wand.display import display

# import Image from wand.image module
from wand.image import Image

# read file using Image function
with Image(filename ="koala.jpeg") as img:
	# perform adaptive blur effect
	# using adaptive_blur() function
	img.selective_blur(radius = 8, sigma = 4,
			threshold = 0.25 * img.quantum_range)

	# save final image
	img.save(filename ="mb_koala.jpeg")

	# display final image
	display(img)
