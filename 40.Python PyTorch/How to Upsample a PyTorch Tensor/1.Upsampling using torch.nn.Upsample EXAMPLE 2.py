#import the necessary library
import torch

# define a tensor and view as a 3D tensor
x = torch.tensor([[1., 2., 3.],
				[4., 5., 6.],
				])
X = x.view(1,1,2,3)
print("Input Tensor Shape:",X.size())
print("Input Tensor:\n",X)

# Upsample with scale_factor 2 and mode = nearest
upsample1 = torch.nn.Upsample(scale_factor=2)
output1 = upsample1(X)
print(upsample1,'\n', output1.shape,'\n', output1)

# # Upsample with scale_factor 3 and mode = bilinear
upsample2 = torch.nn.Upsample(scale_factor=2, mode='bilinear')
output2 = upsample2(X)
print(upsample2,'\n', output2.shape,'\n', output2)

# Upsample with scale_factor 2 and mode = bicubic
upsample3 = torch.nn.Upsample(scale_factor=2, mode='bicubic')
output3 = upsample3(X)
print(upsample3,'\n', output3.shape,'\n', output3)

# Upsample with scale_factor 2 and mode = trilinear
upsample4 = torch.nn.Upsample(scale_factor=3, mode='area')
output4 = upsample4(X)
print(upsample4,'\n', output4.shape,'\n', output4)
