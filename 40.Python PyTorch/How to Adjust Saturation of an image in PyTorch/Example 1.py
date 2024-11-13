# import required library
import torch
import torchvision
import torchvision.transforms as T
import torchvision.transforms.functional as F
from torchvision.io import read_image

# read the image from computer
pic = read_image('Maximum subarray sum modulo m output.png')

# adjust the saturation of the input image
pic = F.adjust_saturation(pic, 10)
pic = T.ToPILImage()(pic)

# display result
pic.show()
