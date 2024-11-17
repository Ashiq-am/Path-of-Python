import matplotlib.pyplot as plt
from scipy import ndimage, misc

# Step 1: Read the image
image_path = 'rose.jpg'
input_image = plt.imread(image_path)

# Step 2: Apply image processing operations
# Example: Gaussian blur with a sigma of 10
blurred_image = ndimage.gaussian_filter(input_image, sigma=10)

# Step 3: Display the original and processed images
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(input_image)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(blurred_image)
axes[1].set_title('Blurred Image')
axes[1].axis('off')

plt.show()
