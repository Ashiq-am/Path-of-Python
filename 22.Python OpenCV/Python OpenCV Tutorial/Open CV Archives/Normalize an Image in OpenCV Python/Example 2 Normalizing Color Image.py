import cv2

# Read color image
image = cv2.imread('kl.png')

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Normalize grayscale image
normalized_gray_image = cv2.normalize(
    gray_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Convert normalized grayscale image back to color
normalized_color_image = cv2.cvtColor(
    normalized_gray_image, cv2.COLOR_GRAY2BGR)

# Display original and normalized images
cv2.imshow('Original Image', image)
cv2.imshow('Normalized Image', normalized_color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
