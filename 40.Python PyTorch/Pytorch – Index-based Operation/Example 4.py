#importing libraries
import torch

a=torch.ones(4,4)#unit vector
t1=torch.randn(2,4)
index3=torch.tensor([1,3])

#copying elements of t1 ensor to 'a' in given order of index
a.index_copy_(0,index3,t1)
