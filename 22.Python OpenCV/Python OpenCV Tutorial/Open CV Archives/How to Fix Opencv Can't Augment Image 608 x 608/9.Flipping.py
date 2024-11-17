# import opencv module
import cv2

# load image
image_path = "path_to_image.png"
image = cv2.imread(image_path)

# resize image
resized_image = cv2.resize(image, (608, 608))

# Horizontal flip
flipped_image = cv2.flip(image_resized, 1)
print(f"Flipped image shape: {flipped_image.shape}")

cv2.imshow("Flipped Image", flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
