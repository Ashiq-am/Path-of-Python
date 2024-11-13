# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:
	img.gamma(1.75)
	img.save(filename ="kl-gamma2.jpeg")
