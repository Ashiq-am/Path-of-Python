from PIL import Image, ImageFilter

img = Image.open(r"sample.png")

# Converting the image to greyscale, as Sobel Operator requires
# input image to be of mode Greyscale (L)
img = img.convert("L")

# Calculating Edges using the passed laplican Kernel
final = img.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8,
										-1, -1, -1, -1), 1, 0))

final.save("EDGE_sample.png")
