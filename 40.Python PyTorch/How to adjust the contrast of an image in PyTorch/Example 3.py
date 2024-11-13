# Import the required libraries
import torch
from PIL import Image
import torchvision.transforms.functional as con

# read the input image from computer
input_img = Image.open('a.png')

# adjust the contrast of the image
input_img = con.adjust_contrast(input_img, 1)

# display result
input_img.show()
