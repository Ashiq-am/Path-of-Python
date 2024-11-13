#importing libraries
import torch

target=torch.zeros([4,4])
indices = torch.LongTensor([[0,1],[1,2],[3,1],[1,0]])#indices to which values to be put
value = torch.ones(indices.shape[0])
#tuple of the index tensor is passed along with the value
target.index_put_(tuple(indices.t()), value)
