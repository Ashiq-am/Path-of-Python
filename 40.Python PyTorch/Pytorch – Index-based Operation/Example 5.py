#importing libraries
import torch

y=torch.ones(5,5)
index1=torch.tensor([0,1,2,3,4])
te=torch.tensor([[1,3,5,7,9],[1,3,5,7,9],[1,3,5,7,9]],dtype=torch.float32)
y.index_copy_(1,index1,te)
