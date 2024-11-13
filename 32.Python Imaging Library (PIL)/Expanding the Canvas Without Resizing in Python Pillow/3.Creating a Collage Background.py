from PIL import Image
import matplotlib.pyplot as plt

# Open the original images
image1 = Image.open("gfg.png")
image2 = Image.open("gfg.png")

# Define the new canvas size (twice the width and height of one image)
new_width = image1.width * 2
new_height = image1.height * 2

# Create a new image with a solid color (white) background
new_image = Image.new("RGB", (new_width, new_height), (255, 255, 255))

# Paste the original images onto the new canvas
new_image.paste(image1, (0, 0))
new_image.paste(image2, (image1.width, 0))

# Display the result using matplotlib
plt.imshow(new_image)
plt.axis('off')  # Hide axes
plt.show()

# Save the result
new_image.save("example.png")
