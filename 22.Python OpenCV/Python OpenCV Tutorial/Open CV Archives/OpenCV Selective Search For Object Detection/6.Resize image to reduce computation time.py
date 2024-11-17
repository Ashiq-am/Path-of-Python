# Calculate a new height
import matplotlib.pyplot as plt
new_height = int(image.shape[1] / 4)
# Calculate a new width
new_width = int(image.shape[0] / 2)
# Resize the image to the new dimensions
resized_image = cv2.resize(image, (new_width, new_height))

# Display the resized image using Matplotlib
plt.imshow(resized_image)
plt.show()
