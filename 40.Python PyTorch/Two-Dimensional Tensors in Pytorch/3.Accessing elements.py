import torch

# defining the tensor
x4=torch.arange(4,13)
y4=x4.view(3,3)

# slicing is performmed
print('First column has the values:{}'.format(y4[:,0]))
print('Second row has the values:{}'.format(y4[1,:]))

# indexing a particular element
print('Data at the index 1,2 :{}'.format(y4[1][2]))
