from pgmagick import Image, DrawableCircle, DrawableText
from pgmagick import Geometry, Color

# draw the image of dimension 600 * 600
img = Image('input.png')

# invoke wave function with amplitude 5 and wavelength 8
img.wave(5, 8)

# invoke write function along with filename
img.write('2_a.png')
