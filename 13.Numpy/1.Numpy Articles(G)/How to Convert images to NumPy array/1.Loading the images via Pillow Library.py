from PIL import Image


# sample.png is the name of the image
# file and assuming that it is uploaded
# in the current directory or we need
# to give the path
image = Image.open('Sample.png')

# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)
