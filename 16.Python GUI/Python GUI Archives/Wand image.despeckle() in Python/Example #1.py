# import Image from wand.imae module
from wand.image import Image

with Image(filename ="koala.jpeg") as img:
	# perform despeckle effect
	img.despeckle()

	# save final image
	img.save(filename ="despeckle_koala.jpg")
