# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# Sepia simulation using sepia_tone() function
	img.sepia_tone(threshold = 0.6)
	img.save(filename ="sepiakoala2.jpeg")
