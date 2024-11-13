# library
from PIL import Image
import matplotlib.pyplot as plt


# opening up of images
img = Image.open("logo.png")
img1 = Image.open("logo2.png")
img.size
img1.size
img_size = img.resize((250, 90))
img1_size = img1.resize((250, 90))

# creating a new image and pasting the
# images
img2 = Image.new("RGB", (250, 180), "white")

# pasting the first image (image_name,
# (position))
img2.paste(img_size, (0, 0))

# pasting the second image (image_name,
# (position))
img2.paste(img1_size, (0, 90))

plt.imshow(img2)
