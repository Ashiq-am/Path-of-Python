import torch
from PIL import Image
import torchvision.transforms as T

image = Image.open('image2.png')

# convert input image to torch tensor
image = T.ToTensor()(image)

# unsqueeze image to make 4D
image = image.unsqueeze(0)

# define avg pooling with square window
# of (kernel_size=5, stride=3)
pooling = torch.nn.AvgPool2d(5, 3)
image = pooling(image)

# squeeze image
image = image.squeeze(0)

# convert tensor to image
image = T.ToPILImage()(image)
image.show()
