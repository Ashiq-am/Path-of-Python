import cv2
import numpy as np

# choose the image file
image = cv2.imread('portrait.jpg')
# get image width and height
height, width = image.shape[:2]
image = cv2.resize(image, (int(width/3), int(height/3)),
                   interpolation=cv2.INTER_AREA)

# greyscale filter
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# place text at center


def place_text(text, image):
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
    text_x = (image.shape[1] - text_size[0]) // 2
    text_y = (image.shape[0] + text_size[1]) // 2
    cv2.putText(image, text, (text_x, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


# place text on the image
place_text('Greyscale image', gray)
place_text('Original image', image)

# show the images together
cv2.imshow('Greyscale image', gray)
cv2.imshow('Original image', image)

# wait for a key press
cv2.waitKey(0)
