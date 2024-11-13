import torch

b=torch.ones(4,4)
t2=torch.randn(4,2)

index4=torch.tensor([0,1])
b.index_copy_(1,index4,t2)
