# import opencv module
import cv2

# load image
image_path = "path_to_image.png"
image = cv2.imread(image_path)

# resize image
resized_image = cv2.resize(image, (608, 608))

print(f"Resized image shape: {resized_image.shape}")
