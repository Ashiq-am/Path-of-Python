import cv2
from google.colab.patches import cv2_imshow

# Read the image in headless mode (without GUI)
image = cv2.imread("o.png", cv2.IMREAD_UNCHANGED)

# Check if the image was successfully read
if image is not None:
    # Display the image (headlessly)
    cv2_imshow(image)
else:
    print("Error: Failed to read the image.")
