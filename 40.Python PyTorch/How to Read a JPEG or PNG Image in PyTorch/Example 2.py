# Import required libraries
import torch
import torchvision
from torchvision.io import read_image
import torchvision.transforms as T

# read the png image
pic = read_image('Maximum subarray sum modulo m output.png')

# convert this torch tensor to PIL image
PIL_img = T.ToPILImage()(pic)

# display result
PIL_img.show()
