# import opencv module
import cv2

# load image path
image_path = "path_to_image.png"
image = cv2.imread(image_path)

if image is None:
    raise ValueError("Image not found or unable to read.")

# Simulate an error where image dimensions are unexpected
if image.shape[:2] != (200, 200):
    raise ValueError("Unexpected image dimensions")
