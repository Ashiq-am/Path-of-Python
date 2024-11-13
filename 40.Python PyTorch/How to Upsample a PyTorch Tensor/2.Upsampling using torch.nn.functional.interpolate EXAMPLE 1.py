# Import the necessary libbraries
import torch

# define a tensor and view as a 3D tensor
x = torch.tensor([[1., 2., 3.],
				[4., 5., 6.],
				])
x = x.view(1,1,2,3)
print("Input Tensor Shape:",x.size())
print("Input Tensor:\n",x)
# apply the upsampling function
y = torch.nn.functional.interpolate(x, scale_factor=2, mode='bilinear')

# print the input and output tensor shapes
print("Output tensor: \n", y.shape,'\n',y)
