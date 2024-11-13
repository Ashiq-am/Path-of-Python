# Inport the necessary module
from PIL import Image
import torch
from torch import nn
from torchvision import transforms

# Read input image
img = Image.open('Ganesh.jpg')

# convert the input image to torch tensor
img = transforms.ToTensor()(img)
print("Input image size:", img.size())

# unsqueeze the image to make it 4D tensor
img = img.unsqueeze(0)
print('unsqueeze Image size',img.shape)

#Kernel
Kernel = torch.tensor([
	[[[1.0, 0.1],[ 0.1, 0.2]],[[ 0.1, 0.2],[ 0.2, 0.3]],[[ 0, 0.1],[0.2, 0.3]]],
	[[[1.0, 0.1],[ 0.1, 0.2]],[[ 0.1, 0.2],[ 0.2, 0.3]],[[ 0, 0.1],[0.2, 0.3]]],
	[[[1.0, 0.1],[ 0.1, 0.2]],[[ 0.1, 0.2],[ 0.2, 0.3]],[[ 0, 0.1],[0.2, 0.3]]],
])

# Kernel shape
print('Kernel Size :',Kernel.shape)


# Transpose convolution Layer
Transpose = nn.ConvTranspose2d(in_channels =3,
							out_channels =2,
							kernel_size=2,
							stride = 2,
							padding=1,
							bias=False)

# Initialize Kernel
Transpose.weight.data = Kernel

# Output value
img2 = Transpose(img)

# squeeze image to make it 3D
img2 = img2.squeeze(0)
print("Output image size:",img2.size())

# convert image to PIL image
img2 = transforms.ToPILImage()(img2)

# display the image after convolution
img2
