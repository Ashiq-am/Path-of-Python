# import required library
import torch

# create two tensors a and b with
# single value
a = torch.tensor(2)
b = torch.tensor(6)

print("Multiplication")
# Normal Multiplication
a.mul(b)

# display content in a
print("Normal Subtraction : ", a.item())

# In-place Multiplication
a.mul_(b)

# display content in a
print("In-place Multiplication : ", a.item())
