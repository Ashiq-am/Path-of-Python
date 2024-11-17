import cv2

# read the image
img = cv2.imread(r"path to image", 0)

# binarize the image
binr = cv2.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]

# define the kernel
kernel = np.ones((3, 3), np.uint8)

# invert the image
invert = cv2.bitwise_not(binr)

# dilate the image
dilation = cv2.dilate(invert, kernel, iterations=1)

# print the output
plt.imshow(dilation, cmap='gray')
