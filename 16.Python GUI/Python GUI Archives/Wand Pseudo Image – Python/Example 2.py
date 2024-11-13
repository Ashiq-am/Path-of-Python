# Import Image from wand.image module
from wand.image import Image

# Create image using Image() and label CROSSHATCH45 for pattern
with Image(width = 100, height = 100, pseudo ='pattern:CROSSHATCH45') as img:

	# Save image
	img.save(filename ='pattern.png')
