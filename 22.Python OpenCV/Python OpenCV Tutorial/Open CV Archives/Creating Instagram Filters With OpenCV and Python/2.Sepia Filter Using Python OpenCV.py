import cv2
import numpy as np

# choose the image file
image = cv2.imread('portrait.jpg')
# get image width and height
height, width = image.shape[:2]
image = cv2.resize(image, (int(width/3), int(height/3)),
                   interpolation=cv2.INTER_AREA)


# sepia filter
sepia = np.array([[0.272, 0.534, 0.131],
                  [0.349, 0.686, 0.168],
                  [0.393, 0.769, 0.189]])
sepia_image = cv2.transform(image, sepia)


# place text at center
def place_text(text, image):
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
    text_x = (image.shape[1] - text_size[0]) // 2
    text_y = (image.shape[0] + text_size[1]) // 2
    cv2.putText(image, text, (text_x, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


# place text on the image
place_text('Original image', image)
place_text('Sepia image', sepia_image)

# show the images together
cv2.imshow('Original image', image)
cv2.imshow('Sepia image', sepia_image)

# wait for a key press
cv2.waitKey(0)
