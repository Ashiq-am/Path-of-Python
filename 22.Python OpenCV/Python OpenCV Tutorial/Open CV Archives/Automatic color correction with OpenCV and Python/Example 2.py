import cv2

# Load the image
img = cv2.imread('image.jpg')

# Convert the image to LAB color space
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Split the LAB image into separate channels
l, a, b = cv2.split(lab)

# Apply CLAHE to the L channel
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
l = clahe.apply(l)

# Merge the LAB channels back together
lab = cv2.merge((l,a,b))

# Convert the LAB image back to RGB color space
output = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

# Display the result
cv2.imshow('Color space conversion ', output)
cv2.waitKey(0)
