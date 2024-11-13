from pgmagick import Image

#Include full path to the input image
img = Image('input_image.jpg')
img.filterType(FilterTypes.SincFilter)
img.resize('150x150')
img.write('output_image.jpg')
