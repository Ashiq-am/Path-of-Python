# import opencv module
import cv2

# Attempt to load image
image_path = "path_to_non_existing_image.png"
image = cv2.imread(image_path)

# This might fail if the image path is incorrect or the image is corrupted
if image is None:
    raise ValueError("Image not found or unable to load")
