from wand.image import Image

# Read image using Image function
with Image(filename ="man.jpeg") as img:
	with img.clone() as fimg:
		# flopped image using flop() function
		fimg.flop()
		fimg.save(filename ='manflopped.jpeg')
