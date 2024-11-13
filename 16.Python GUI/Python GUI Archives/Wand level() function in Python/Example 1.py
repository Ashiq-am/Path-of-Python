# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:
	img.level(0.2, 0.9, gamma = 1.1)
	img.save(filename ="kl-level.jpeg")
