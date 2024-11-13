# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# solarized image using solarize() function
	img.solarize(threshold = 0.5 * img.quantum_range)
	img.save(filename ="solpkoala.jpeg")
