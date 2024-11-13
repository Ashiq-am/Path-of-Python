# Import Image from wand.image module
from wand.image import Image

# Import display to display final image
from wand.display import display

# Read image using Image function
with Image(filename ='koala.jpeg') as img:

	# using transform() function
	img.transform('50 %')

	# Saving image
	img.save(filename ='transform1.jpeg')

	# display image
	display(img)
