# Import required libraries
import torch
import torchvision
from torchvision.io import read_image
import torchvision.transforms as T

# read the jpg image
pic = read_image('img.jpg')

# convert this torch tensor to PIL image
PIL_img = T.ToPILImage()(pic)

# display result
PIL_img.show()
