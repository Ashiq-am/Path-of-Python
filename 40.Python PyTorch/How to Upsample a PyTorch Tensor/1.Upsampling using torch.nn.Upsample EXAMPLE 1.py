#import the necessary library
import torch

# define a tensor and view as a 3D tensor
x = torch.tensor([1., 2.])
X = x.view(1,1,2)
print("Input Tensor Shape:",X.size())
print("Input Tensor:",X)

# Upsample with scale_factor 2 and mode = nearest
upsample1 = torch.nn.Upsample(scale_factor=2)
output1 = upsample1(X)
print(upsample1,'-->>', output1)

# # Upsample with scale_factor 3 and mode = nearest
upsample2 = torch.nn.Upsample(scale_factor=3)
output2 = upsample2(X)
print(upsample2,'-->>', output2)

# Upsample with scale_factor 2 and mode = linear
upsample3 = torch.nn.Upsample(scale_factor=2, mode='linear')
output3 = upsample3(X)
print(upsample3,' -->>', output3)
