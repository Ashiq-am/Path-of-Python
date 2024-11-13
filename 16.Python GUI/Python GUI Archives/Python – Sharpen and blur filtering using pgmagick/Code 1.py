# importing library
from pgmagick import Image

img = Image('koala.jpg')

# sharpening image
img.sharpen(2)
img.write('sharp_koala.jpg')
