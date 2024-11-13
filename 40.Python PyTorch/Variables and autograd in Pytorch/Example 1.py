# importing libraries
import torch
from torch.autograd import Variable

# packing the tensors with Variable
a = Variable(torch.tensor([5., 4.]), requires_grad=True)
b = Variable(torch.tensor([6., 8.]))

# polynomial function with a,b as variable
y = ((a**2)+(5*b))
z = y.mean()
print('Z value is:', z)
