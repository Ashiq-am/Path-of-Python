# Python OpenCV - getgaussiankernel() Function

# import cv2
import cv2

# read image
img = cv2.imread('gfg_logo.png')

# Creates a 1-D Gaussian kernel
a = cv2.getGaussianKernel(7, 1)

# print Gaussian filter coefficients matrix
print(a)
