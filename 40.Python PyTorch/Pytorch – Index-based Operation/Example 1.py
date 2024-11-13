#importing libraries
import torch

x=torch.zeros(5,5)
te=torch.tensor([[1,3,5,7,9],[1,3,5,7,9],[1,3,5,7,9]],dtype=torch.float32)
index0=torch.tensor([0,2,4])
#adding tensor te to x along row of the given order
x.index_add_(0,index0,te)
