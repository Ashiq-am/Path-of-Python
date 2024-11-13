from pgmagick import Image, DrawableCircle, DrawableText
from pgmagick import Geometry, Color

# draw the image of dimension 600 * 600
img = Image('input.png')

# invoke shade function with azimuthal angle as 45 and angle of elevation as 90
img.shade(45, 90)

# invoke write function along with filename
img.write('2_a.png')
