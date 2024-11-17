# vertically concatenates images
# of same width
import cv2

im_v = cv2.vconcat([img1, img1])

# show the output image
cv2.imshow('sea_image.jpg', im_v)
