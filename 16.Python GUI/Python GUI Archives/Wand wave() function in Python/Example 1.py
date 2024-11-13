# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# rippled image using vignette() function
	img.wave(amplitude = img.height / 32,
			wave_length = img.width / 4)
	img.save(filename ="wkoala2.jpeg")
