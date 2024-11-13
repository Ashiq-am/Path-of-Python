# Import the required libraries
import torch
import torchvision
from torchvision.io import read_image
from torchvision.utils import draw_bounding_boxes

# read input image from your computer
img = read_image('a3.png')

# create boxes
box_1 = [330, 220, 450, 350]
box_2 = [530, 200, 650, 320]
box = [box_1, box_2]
box = torch.tensor(box, dtype=torch.int)

# draw bounding box and fill color
img = draw_bounding_boxes(img, box, width=5, colors=[
						"orange", "blue"], fill=True)

# transform this image to PIL image
img = torchvision.transforms.ToPILImage()(img)

# display output
img.show()
