# Create an initial mask
mask = np.zeros(image.shape[:2], np.uint8)

# Create temporary arrays used by the algorithm
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Define the rectangle around the object
rect = (50, 50, image.shape[1] - 70, image.shape[0] - 70)

# Apply GrabCut algorithm with the rectangle
cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 10, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Multiply the original image with the new mask to remove the background
image = image * mask2[:, :, np.newaxis]
