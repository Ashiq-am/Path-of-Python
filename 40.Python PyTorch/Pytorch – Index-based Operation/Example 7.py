#importing libraries
import torch
c=torch.randn(4,4)

index5=torch.tensor([0,2])

#filling 4 within the elements of the tensor 'c' along the indices 0,2
c.index_fill_(0,index5,4)
print(c)
