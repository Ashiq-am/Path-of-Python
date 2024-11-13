# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:
	img.level(0.5, 0.7, gamma = 1.1)
	img.save(filename ="kl-level2.jpeg")
