import imageio
import matplotlib.pyplot as plt

# Step 1: Read the image
image_path = 'rose.jpg'
input_image = imageio.imread(image_path)

# Step 2: Plot the image
plt.imshow(input_image)
plt.axis('off') # Turn off axis
plt.show()
