# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:
	img.evaluate(operator ='leftshift', value = 1, channel ='red')
	img.save(filename ="kl-enhanced2.jpeg")
