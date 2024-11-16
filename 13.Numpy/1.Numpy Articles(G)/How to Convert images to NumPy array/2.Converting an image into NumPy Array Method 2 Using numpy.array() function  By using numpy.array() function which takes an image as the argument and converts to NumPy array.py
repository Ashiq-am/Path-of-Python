from PIL import Image
import numpy


img= Image.open("Sample.png")
np_img = numpy.array(img)

print(np_img.shape)
