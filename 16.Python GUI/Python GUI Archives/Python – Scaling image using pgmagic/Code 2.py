# importing library
from pgmagick import Image, Blob

img = Image(Blob(open('koala.jpeg').read()))

# scaling image
img.scale('250x200')
img.write('scale_koala.jpeg')
