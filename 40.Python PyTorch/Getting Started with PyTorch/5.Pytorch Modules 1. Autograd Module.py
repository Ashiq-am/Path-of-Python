# importing torch
import torch

# creating a tensor
t1=torch.tensor(1.0, requires_grad = True)
t2=torch.tensor(2.0, requires_grad = True)

# creating a variable and gradient
z=100 * t1 * t2
z.backward()

# printing gradient
print("dz/dt1 : ", t1.grad.data)
print("dz/dt2 : ", t2.grad.data)
