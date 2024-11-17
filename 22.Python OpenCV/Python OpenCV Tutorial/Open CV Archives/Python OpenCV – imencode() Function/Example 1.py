# This code demonstrates encoding of image.
import numpy as np
import cv2 as cv

# Passing path of image as parameter
img = cv.imread('/content/gfg.png')

# If the extension of our image was
# '.jpg' then we have passed it as
# argument instead of '.png'.
img_encode = cv.imencode('.png', img)[1]

# Converting the image into numpy array
data_encode = np.array(img_encode)

# Converting the array to bytes.
byte_encode = data_encode.tobytes()

print(byte_encode)
