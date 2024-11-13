from PIL import Image
from PIL import ImageEnhance

# Opens the image file
image = Image.open('gfg.png')

# shows image in image viewer
image.show()


# Enhance Contrast
curr_con = ImageEnhance.Contrast(image)
new_con = 0.3

# Contrast enhanced by a factor of 0.3
img_contrasted = curr_con.enhance(new_con)

# shows updated image in image viewer
img_contrasted.show()
