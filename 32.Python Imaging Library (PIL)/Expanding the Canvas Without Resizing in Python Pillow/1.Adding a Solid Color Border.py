from PIL import Image
import matplotlib.pyplot as plt

# Open the original image
original_image = Image.open("gfg.png")

# Define the new canvas size
border_size = 50
new_width = original_image.width + 2 * border_size
new_height = original_image.height + 2 * border_size

# Create a new image with a solid color (white) background
new_image = Image.new("RGB", (new_width, new_height), (255, 255, 255))

# Paste the original image onto the center of the new image
new_image.paste(original_image, (border_size, border_size))

# Display the result using matplotlib
plt.imshow(new_image)
plt.axis('off')  # Hide axes
plt.show()

# Save the result
new_image.save("example.png")
