# Calculating the center of the image
from email.mime import image
from turtledemo.chaos import h

import cv2
from numpy import w

center = (w // 2, h // 2)

# Generating a rotation matrix
matrix = cv2.getRotationMatrix2D(center, -45, 1.0)

# Performing the affine transformation
rotated = cv2.warpAffine(image, matrix, (w, h))
