#importing libraries
import torch

y=torch.ones(5,5)#unitvector
index2=torch.tensor([0,1,1,1,2])
ten=torch.randn(1,5)
#adding values to y along the column with given order
y.index_add_(1,index2,ten)
