import cv2

# Read grayscale image
image = cv2.imread('kl.png', cv2.IMREAD_GRAYSCALE)

# Normalize image
normalized_image = cv2.normalize(
    image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Display original and normalized images
cv2.imshow('Original Image', image)
cv2.imshow('Normalized Image', normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
