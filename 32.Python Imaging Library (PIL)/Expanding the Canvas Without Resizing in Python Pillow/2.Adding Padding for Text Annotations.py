from PIL import Image
import matplotlib.pyplot as plt

# Open the original image
original_image = Image.open("gfg.png")

# Define the new canvas size
padding_size = 100
new_width = original_image.width
new_height = original_image.height + padding_size

# Create a new image with a solid color (white) background
new_image = Image.new("RGB", (new_width, new_height), (255, 255, 255))

# Paste the original image onto the top of the new image
new_image.paste(original_image, (0, 0))

# Display the result using matplotlib
plt.imshow(new_image)
plt.axis('off')  # Hide axes
plt.show()

# Save the result
new_image.save("example.png")
