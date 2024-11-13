# Import Image from wand.image module
from wand.image import Image

frequency = 3
phase_shift = -90
amplitude = 0.2
bias = 0.7

# Read image using Image function
with Image(filename ="road.jpeg") as img:
	# appying sinusoid FUCTION_TYPE
	img.function('polynomial', [frequency, phase_shift, amplitude, bias])
	img.save(filename ="rd-functioned.jpeg")
