from wand.image import Image

# Read image using Image function
with Image(filename ="man.jpeg") as img:
	with img.clone() as fimg:
		# flip image using flip() function
		fimg.flip()
		fimg.save(filename ='manflipped.jpeg')
