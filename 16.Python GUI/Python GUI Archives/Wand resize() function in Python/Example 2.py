# import required libraries
import urllib3
from cStringIO import StringIO
from wand.image import Image
from wand.display import display

# load image from url
http = urllib3.PoolManager()
r = http.request('GET', 'https://media.geeksforgeeks.org/wp-content/uploads/geeksforgeeks-6.png')
f = StringIO(r.data)

# read image using Image() function
with Image(file=f) as img:

	# resize image using resize() function
	img.resize(400, 300)

	# save image
	img.save(filename = 'gogurl.png')

	# display final image
	display(img)
