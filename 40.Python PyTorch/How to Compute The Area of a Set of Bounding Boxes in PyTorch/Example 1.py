# Import the required libraries
import torch
import torchvision
from torchvision.io import read_image
from torchvision.utils import draw_bounding_boxes
from torchvision.ops import box_area

# read input image from your computer
img = read_image('Maximum subarray sum modulo m output.png')

# bounding box are xmin, ymin, xmax, ymax
b_box = [80, 70, 500, 200]

# convert the bounding box to torch tensor
b_box = torch.tensor(b_box, dtype=torch.int)

# unsqueeze the given bounding box to make
# it 2D tensor
b_box = b_box.unsqueeze(0)

# Compute the bounding box area
area = box_area(b_box)

# set this computed area on label
label = [f"b_box area = {area.item()}"]

# draw the above define bounding box on image
# Set the above define label on image
img = draw_bounding_boxes(img, b_box, labels=label,
						width=4, colors=(255, 0, 0))


# transform this image to PIL image
img = torchvision.transforms.ToPILImage()(img)

# display result
img.show()
