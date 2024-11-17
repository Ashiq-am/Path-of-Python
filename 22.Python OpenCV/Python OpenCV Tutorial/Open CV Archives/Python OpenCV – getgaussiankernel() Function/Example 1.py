# Python OpenCV - getgaussiankernel() Function

# import cv2
import cv2

# read image
img = cv2.imread('gfg2.jpg')

# Creates a 1-D Gaussian kernel
a = cv2.getGaussianKernel(3, 1)

# print Gaussian filter coefficients matrix
print(a)
