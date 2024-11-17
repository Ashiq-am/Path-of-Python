# import opencv and numpy module
import cv2
import numpy as np

image_path = "path_to_image.png"

# Simulate wrong data type
image = cv2.imread(image_path).astype(np.float32)

if image.dtype != 'uint8':
    raise TypeError("Incorrect image data type")

# Convert to correct data type
image = image.astype('uint8')
print(f"Image dtype after correction: {image.dtype}")
