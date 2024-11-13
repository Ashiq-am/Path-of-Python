import torch

# tensor with 3 dimension
x=torch.tensor([[[11,12,13],[14,15,16],[17,18,19]]])

# 1d tensor
x1=torch.arange(10,19)

# reshaping it to 3d tensor
x1=x1.view(1,3,3)
print(x,'\n',x1)
