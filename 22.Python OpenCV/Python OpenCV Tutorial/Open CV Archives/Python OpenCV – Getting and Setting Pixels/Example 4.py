import cv2
img = cv2.imread('image.png', 0)


# shape prints the tuple (height,weight,channels)
print("image shape = ", img.shape)

# img will be a numpy array of the above shape
print("image array = ", img)

print("pixel at index (5,5): ", img[5][5])
