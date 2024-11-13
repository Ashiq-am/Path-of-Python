# import required library
import torch

# create two tensors a and b with
# single value
a = torch.tensor(2)
b = torch.tensor(6)

print("Subtraction")
# Normal Subtraction
a.sub(b)

# display content in a
print("Normal Subtraction : ", a.item())

# In-place Subtraction
a.sub_(b)

# display content in a
print("In-place Subtraction : ", a.item())
