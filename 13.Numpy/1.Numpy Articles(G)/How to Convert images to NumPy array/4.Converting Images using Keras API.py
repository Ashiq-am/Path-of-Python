from keras.preprocessing.image import load_img
import warnings

# load the image via load_img
# function
img = load_img('sample.png')

# details about the image printed below
print(type(img))
print(img.format)
print(img.mode)
print(img.size)
