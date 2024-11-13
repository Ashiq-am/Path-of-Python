# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="road.jpeg") as img:
	img.statistic("median", width = 8, height = 5)
	img.save(filename ="rd-statistic.jpg")
