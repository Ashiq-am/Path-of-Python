# import required library
import torch

# create two tensors a and b with
# 4 values each
a = torch.tensor([2, 3, 4, 5])
b = torch.tensor([2, 3, 4, 5])

print("Addition")
# Normal addition
a.add(b)

# display content in a
print("Normal addition : ", a)

# In-place addition
a.add_(b)

# display content in a
print("In-place addition : ", a)


print("\nMultiplication")

# Normal Multiplication
a.mul(b)

# display content in a
print("Normal Subtraction : ", a)

# In-place Multiplication
a.mul_(b)

# display content in a
print("In-place Multiplication : ", a)
print()
