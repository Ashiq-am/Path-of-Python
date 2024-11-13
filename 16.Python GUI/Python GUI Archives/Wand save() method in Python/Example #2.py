# import gzip
import gzip

# import Image from wand.image module
from wand.image import Image

# create gz compressed file
gz = gzip.open('koala.jpg.gz')

# read image using Image() function
with Image(filename ='pikachu.png') as img:
	# get format of image
	img.format = 'jpeg'

	# save image to output stream using save() function
	img.save(file = gz)
gz.close()
