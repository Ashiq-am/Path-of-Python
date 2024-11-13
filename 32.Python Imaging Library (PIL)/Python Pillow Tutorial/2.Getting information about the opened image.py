from PIL import Image


# Location of the image
img = Image.open("geek.jpg")

# size of the image
print(img.size)

# format of the image
print(img.format)
