# importing library
from pgmagick.api import Image

img = Image('gog.png')

# scaling image
img.scale((150, 100), 'lanczos')
img.write('scale_gog.png')
