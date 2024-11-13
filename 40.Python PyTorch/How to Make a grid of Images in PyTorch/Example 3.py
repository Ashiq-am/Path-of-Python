# import required library
import torch
import torchvision
from torchvision.io import read_image
from torchvision.utils import make_grid

# read images from computer
a = read_image('a.png')
b = read_image('b.png')
c = read_image('c.png')
d = read_image('d.png')
e = read_image('e.png')
f = read_image('f.png')

# make grid from the input images
# set nrow=3, and padding=25
Grid = make_grid([a, b, c, d, e, f], nrow=3, padding=25)

# display result
img = torchvision.transforms.ToPILImage()(Grid)
img.show()
