# importing libraries
import torch
from torch.autograd import Variable

# creating random tensors for weights and wrap them in variables
x = Variable(torch.randn(1, 10), requires_grad=False)
W = Variable(torch.randn(10, 1), requires_grad=True) # weight matrix
b = Variable(torch.randn(1), requires_grad=True) # bias vector
y = Variable(torch.tensor([[0.822]]))

# performing matrix multiplication to compute output
y_pred = torch.matmul(x, W)+b

# calculating loss
loss = (y_pred-y).pow(2)
print(loss)

# computing gradient
loss.backward()

print(W.grad)
print(b.grad)

lr = 0.001

# updating the weight matrix after backpropagation
with torch.no_grad():
	W = W-(lr*W.grad.data)
print(W)
