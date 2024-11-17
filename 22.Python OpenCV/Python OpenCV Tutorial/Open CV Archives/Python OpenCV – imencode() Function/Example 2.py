import numpy as np
import cv2 as cv

img = cv.imread('/content/OpenCV.png')
img_encode = cv.imencode('.jpg', img)[1]

data_encode = np.array(img_encode)
byte_encode = data_encode.tobytes()

print(byte_encode)
