# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:
	img.evaluate(operator ='rightshift', value = 1, channel ='blue')
	img.save(filename ="kl-enhanced.jpeg")
