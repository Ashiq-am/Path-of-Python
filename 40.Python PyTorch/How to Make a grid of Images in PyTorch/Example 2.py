# import required library
import torch
import torchvision
from torchvision.io import read_image
from torchvision.utils import make_grid

# read images from computer
a = read_image('a.jpg')
b = read_image('b.jpg')
c = read_image('c.jpg')
d = read_image('d.jpg')
e = read_image('e.jpg')
f = read_image('f.jpg')

# make grid from the input images
# this grid contain 2 rows and 3 columns
Grid = make_grid([a, b, c, d, e, f], nrow=3)

# display result
img = torchvision.transforms.ToPILImage()(Grid)
img.show()
