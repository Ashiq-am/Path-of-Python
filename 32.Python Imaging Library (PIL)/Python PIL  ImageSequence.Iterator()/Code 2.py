

# importing Image class from PIL package
from PIL import Image, ImageSequence

# creating a object
im = Image.open(r"C:\Users\System-Pc\Desktop\tree.jpg")
index = 1
for frame in ImageSequence.Iterator(im):
	frame.save("frame % d.jpg" % index)
	index = index + 1

im.getdata()
im.show()
