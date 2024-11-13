# import required library
import torch

# create two tensors a and b with
# single value
a = torch.tensor(2)
b = torch.tensor(6)

print("Addition")
# Normal addition
a.add(b)

# display content in a
print("Normal addition : ", a.item())

# In-place addition
a.add_(b)

# display content in a
print("In-place addition : ", a.item())
