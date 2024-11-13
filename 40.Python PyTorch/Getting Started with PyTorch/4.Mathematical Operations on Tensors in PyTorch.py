# import torch module
import torch

# defining two tensors
t1 = torch.tensor([1, 2, 3, 4])
t2 = torch.tensor([5, 6, 7, 8])

# adding two tensors
print("tensor2 + tensor1")
print(torch.add(t2, t1))

# subtracting two tensor
print("\ntensor2 - tensor1")
print(torch.sub(t2, t1))

# multiplying two tensors
print("\ntensor2 * tensor1")
print(torch.mul(t2, t1))

# diving two tensors
print("\ntensor2 / tensor1")
print(torch.div(t2, t1))
