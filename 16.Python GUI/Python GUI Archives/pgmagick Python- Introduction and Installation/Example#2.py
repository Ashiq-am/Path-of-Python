from pgmagick import Image

#Include full path to the input image
img = Image('input_image.jpg')
img.quality(100)
img.scale('100x100')
img.sharpen(1.0)
img.write('output_image.jpg')
