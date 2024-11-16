# Import the necessary libraries
from PIL import Image
from numpy import asarray


# load the image and convert into
# numpy array
img = Image.open('Sample.png')
numpydata = asarray(img)

print(type(numpydata))

# shape
print(numpydata.shape)

# Below is the way of creating Pillow
# image from our numpyarray
pilImage = Image.fromarray(numpydata)
print(type(pilImage))

# Let us check image details
print(pilImage.mode)
print(pilImage.size)
