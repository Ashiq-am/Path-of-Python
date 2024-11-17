import matplotlib.pyplot as plt
from skimage import io, color, filters

# Step 1: Read the image
image_path = 'rose.jpg'
input_image = io.imread(image_path)

# Step 2: Apply image processing operations (e.g., edge detection)
edges = filters.sobel(input_image)

# Step 3: Display the original and processed images
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(input_image)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(edges, cmap='gray')
axes[1].set_title('Edge Detection')
axes[1].axis('off')

plt.show()
