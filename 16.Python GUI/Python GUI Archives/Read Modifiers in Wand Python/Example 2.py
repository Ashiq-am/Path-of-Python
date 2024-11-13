# Import Image from wand.image module
from wand.image import Image

# Read first six frames of gif using Image() function
with Image(filename='sample.gif[0-5]') as f:
	#save final image
	f.save(filename = "final.gif")
