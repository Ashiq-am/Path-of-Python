# Read image
# You can put your input image over here
# to run bicubic interpolation
# The read function of Open CV is used
# for this task
import cv2

img = cv2.imread('gfg.png')

# Scale factor
ratio = 2

# Coefficient
a = -1/2

# Passing the input image in the
# bicubic function
dst = bicubic(img, ratio, a)
print('Completed!')

# Saving the output image
cv2.imwrite('bicubic.png', dst)
bicubicImg=cv2.imread('bicubic.png')
