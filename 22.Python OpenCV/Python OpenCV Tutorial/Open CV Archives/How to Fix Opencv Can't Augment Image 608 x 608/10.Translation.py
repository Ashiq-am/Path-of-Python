# import opencv and numpy module
import cv2
import numpy as np

# load image
image_path = "path_to_image.png"
image = cv2.imread(image_path)

# resize image
resized_image = cv2.resize(image, (608, 608))

# funtion to translate image
def translate_image(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

translated_image = translate_image(resized_image, 100, 50)
print(f"Translated image shape: {translated_image.shape}")

# displaying image
cv2.imshow("Rotated Image", translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
