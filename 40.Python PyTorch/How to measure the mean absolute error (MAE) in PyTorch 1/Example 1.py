# Import required libraries
import torch
import torch.nn as nn

# create input tensors
input_tensor = torch.tensor([1.4725, -0.4241, -0.3799, 0.3451])

# create target tensors
target_tensor = torch.tensor([1.3913, -0.4572, -0.2346, 1.4708])

# print above created tensors
print("\n Input tensor: \n", input_tensor)
print("\n Target tensor: \n", target_tensor)

# use L1Loss() method to create a criterion
# to measure the mean absolute error.
MAE = nn.L1Loss()

# compute the mean absolute error
output_tensor = MAE(input_tensor, target_tensor)

# print result
print("\n MAE loss: ", output_tensor)
