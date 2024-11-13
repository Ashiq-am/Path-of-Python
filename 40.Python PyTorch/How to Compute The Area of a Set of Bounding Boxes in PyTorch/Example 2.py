# Import the required libraries
import torch
from PIL import Image
import torchvision
from torchvision.io import read_image
from torchvision.utils import draw_bounding_boxes
from torchvision.ops import box_area

# read input image from your computer
img = read_image('Maximum subarray sum modulo m output.png')

# create boxes
b_box1 = [80, 70, 500, 200]
b_box2 = [80, 230, 500, 300]
b_box3 = [580, 70, 720, 300]
b_box = [b_box1, b_box2,b_box3]

# convert the bounding box to torch tensor
b_box = torch.tensor(b_box, dtype=torch.int)

# Compute the bounding box area
area = box_area(b_box)

# set this computed area on label
labels = [f"b_box area ={n}" for n in area]

# draw the above define bounding boxes on image
img=draw_bounding_boxes(img, b_box, labels = labels, width=4,
						colors=["orange", "white","red"])

# transform this image to PIL image
img = torchvision.transforms.ToPILImage()(img)

# display result
img.show()
