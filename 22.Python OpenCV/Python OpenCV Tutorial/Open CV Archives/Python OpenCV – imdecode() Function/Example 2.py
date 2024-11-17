# import necessary modules
import numpy as np
import urllib.request
import cv2

# read image url
url = 'https://media.geeksforgeeks.org/wp-content/uploads/20211003151646/geeks14.png'

with urllib.request.urlopen(url) as resp:
    # convert to numpy array
    image = np.asarray(bytearray(resp.read()), dtype="uint8")

    # 0 is used for grayscale image
    image = cv2.imdecode(image, 0)

    # display image
    cv2.imwrite("result.jpg", image)
