from pgmagick import Image, DrawableCircle, DrawableText
from pgmagick import Geometry, Color

# draw the image of dimension 600 * 600
img = Image('input.png')

# invoke contrast() function
img.contrast(27)

# invoke write function along with filename
img.write('2_a.png')
