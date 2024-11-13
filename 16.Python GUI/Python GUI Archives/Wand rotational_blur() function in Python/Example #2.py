# import display() to show final image
from wand.display import display

# import Image from wand.image module
from wand.image import Image

# read file using Image function
with Image(filename ="koala.jpeg") as img:

	# perform adaptive blur effect using adaptive_blur() function
	img.rotational_blur(angle = 30)

	# save final image
	img.save(filename ="gb_koala.jpeg")

	# display final image
	display(img)
