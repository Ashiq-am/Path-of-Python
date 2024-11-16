# Import required modules
import numpy
from PIL import Image
import numpy as np

# Load image
image = Image.open('W3.jpg')

# Convert image to array
image_arr = numpy.array(image)

# Crop image
image_arr = image_arr[700:1400, 1450:2361]

# Convert array to image
image = Image.fromarray(image_arr)

# Display image
image.show()
