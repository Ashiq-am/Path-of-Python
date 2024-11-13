# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open(r"C:\Users\sadow984\Desktop\download2.JPG")

# applying the rank filter
im2 = im1.filter(ImageFilter.RankFilter(size=3, rank=(3 * 3) // 2))

im2.show()
