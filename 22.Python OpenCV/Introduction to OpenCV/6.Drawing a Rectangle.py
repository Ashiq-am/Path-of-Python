# We are copying the original image,
# as it is an in-place operation.
from email.mime import image

import cv2

output = image.copy()

# Using the rectangle() function to create a rectangle.
rectangle = cv2.rectangle(output, (1500, 900),
						(600, 400), (255, 0, 0), 2)
