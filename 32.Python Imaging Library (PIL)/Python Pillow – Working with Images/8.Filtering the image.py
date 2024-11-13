# Import required image modules
from PIL import Image, ImageFilter

# Import all the enhancement filter from pillow
from PIL.ImageFilter import (
BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

# Create image object
img = Image.open('nature.jpg')

# Applying the sharpen filter
# You can change the value in filter function
# to see the deifferences
img1 = img.filter(SHARPEN)
img1.show()
