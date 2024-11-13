#importing libraries
import torch

m=torch.randn(3,4)
print('Original matrix:\n',m)
indices=torch.tensor([0,1])
print("Indexed Matrix:\n",torch.index_select(m, 0, indices))
