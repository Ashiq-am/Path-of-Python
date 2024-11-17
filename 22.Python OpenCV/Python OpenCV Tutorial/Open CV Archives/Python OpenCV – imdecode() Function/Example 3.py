# import necessayr modules
import numpy as np
import urllib.request
import cv2

# read th image
with open("image.jpg", "rb") as image:
    f = image.read()

    # convert to numpy array
    image = np.asarray(bytearray(f))

    # RGB to Grayscale
    image = cv2.imdecode(image, 0)

    # display image
    cv2.imshow("output", image)
