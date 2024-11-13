# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:

	# denoise image using wave_denoise() function
	img.wavelet_denoise(threshold = 0.05 * img.quantum_range,
						softness = 0.0)
	img.save(filename ="vkoala.jpeg")
