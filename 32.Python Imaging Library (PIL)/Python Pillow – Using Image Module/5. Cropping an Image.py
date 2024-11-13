from PIL import Image

# open image and get size
img = Image.open("gfg.jpg")
width, height = img.size

# cropped image using corrdinates
area = (0, 0, width/2, height/2)
crop_img = img.crop(area)
crop_img.save("cropped_image.jpg")
