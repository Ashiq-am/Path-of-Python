from PIL import Image


size = (40, 40)
img = Image.open(r"test.png")
r_img = img.resize(size, resample = Image.BILINEAR)

# resized_test.png => Destination_path
r_img.save("resized_test.png")

# Opening the new image
img = Image.open(r"resized_test.png")
print(img.size)
