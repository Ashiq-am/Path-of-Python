# import Image from wand.image module
from wand.image import Image
from wand.display import display

# read file using Image function
with Image(filename ="human1.jpeg") as img:

	# perform blur effect using blur() function
	img.blur(radius = 3, sigma = 4, )

	# save final image
	img.save(filename ="blurhuman.jpeg")
	display(img)
