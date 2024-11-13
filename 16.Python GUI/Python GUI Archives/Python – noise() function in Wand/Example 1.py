# Import Image from wand.image module
from wand.image import Image

# Read image using Image() function
with Image(filename ="koala.jpeg") as img:

	# Generate noise image using spread() function
	img.noise("poisson", attenuate = 0.9)
	img.save(filename ="noisekoala.jpeg")
