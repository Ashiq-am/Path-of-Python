# Calculating the ratio
from email.mime import image
from turtledemo.chaos import h

import cv2
from numpy import w

ratio = 800 / w

# Creating a tuple containing width and height
dim = (800, int(h * ratio))

# Resizing the image
resize_aspect = cv2.resize(image, dim)
