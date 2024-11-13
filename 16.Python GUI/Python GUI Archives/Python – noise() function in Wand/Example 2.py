# Import Image from wand.image module
from wand.image import Image

# Read image using Image() function
with Image(filename ="koala.jpeg") as img:

	# Generate noise image using spread() function
	img.noise("laplacian", attenuate = 1.0)
	img.save(filename ="noisekoala2.jpeg")
