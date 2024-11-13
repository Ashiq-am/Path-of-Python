# import required module
import cv2
import matplotlib.pyplot as plt

# read image
image = cv2.imread('gfg.png')

# call imshow() using plt object
plt.imshow(image)

# display that image
plt.show()
