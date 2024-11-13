# importing library
from pgmagick.api import Image

img = Image('koala.jpeg')

# blur image
img.blur(10, 5)
img.write('blur_koala.jpeg')
