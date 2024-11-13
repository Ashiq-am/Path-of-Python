from pgmagick import Image, DrawableCircle, DrawableText
from pgmagick import Geometry, Color

# draw the image of dimension 600 * 600
img = Image((600, 600), "gradient:# ffffff-# 12323e")

# invoke write function along with filename
img.write('1_a.png')
