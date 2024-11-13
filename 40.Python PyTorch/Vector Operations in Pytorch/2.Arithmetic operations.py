# importing pytorch module
import torch

# create an vector A
A = torch.tensor([58, 59, 60, 61, 62])

# create an vector B
B = torch.tensor([100, 120, 140, 160, 180])

# add two vectors
print("Addition of two vectors:", A+B)

# subtract two vectors
print("subtraction of two vectors:", A-B)

# multiply two vectors
print("multiplication of two vectors:", A*B)

# multiply two vectors
print("multiplication of two vectors:", A*B)

# divide two vectors
print("division of two vectors:", A/B)

# floor divide two vectors
print("floor division of two vectors:", A//B)

# modulous of two vectors
print("modulous operation of two vectors:", A % B)

# power of two vectors
print("power operation of two vectors:", A**B)
