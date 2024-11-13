# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# vignette image using vignette() function
	img.wavelet_denoise(threshold = 0.065 * img.quantum_range,
						softness = 0.00)
	img.save(filename ="vkoala2.jpeg")
