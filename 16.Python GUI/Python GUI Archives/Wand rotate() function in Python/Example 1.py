# Import Image from wand.image module
from wand.image import Image

with Image(filename ="koala.jpeg") as img:
	with img.clone() as rotated:
		# rotate image using rotate() function
		rotated.rotate(90)
		rotated.save(filename ='transform-rotated-90.jpg')
