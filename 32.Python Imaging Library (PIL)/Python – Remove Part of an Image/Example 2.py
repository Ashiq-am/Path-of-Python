# Importing ImageDraw for
# using floodfill function
from PIL import Image, ImageDraw

# Opening the image and
# converting its type to RGBA
img = Image.open(r"IMG_PATH").convert('RGBA')

# Location of seed
seed = (0, 0)

# Pixel Value which would
# be used for replacement
rep_value = (0, 0, 0, 0)

# Calling the floodfill() function and
# passing it image, seed, value and
# thresh as arguments
ImageDraw.floodfill(img, seed, rep_value, thresh = 100)

img.show()
