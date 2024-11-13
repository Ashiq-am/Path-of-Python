

# importing Image class from PIL package
from PIL import Image, ImageSequence

# creating a object
im = Image.open(r"C:\Users\System-Pc\Desktop\home.png")
index = 1
for frame in ImageSequence.Iterator(im):
	frame.save("frame % d.png" % index)
	index = index + 1

im.getdata()
im.show()
