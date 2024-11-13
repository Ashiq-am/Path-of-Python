from PIL import Image

img1 = Image.open(r"BACKGROUND_IMAGE_PATH")
img2 = Image.open(r"OVERLAY_IMAGE_PATH")

# No transparency mask specified,
# simulating an raster overlay
img1.paste(img2, (0,0))

img1.show()
