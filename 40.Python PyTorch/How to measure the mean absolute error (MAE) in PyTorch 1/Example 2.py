# Import required libraries
import torch
import torch.nn as nn

# create input tensors
input_tensor = torch.tensor([[-1.4576, 0.6496, 0.6783],
							[0.4895, 1.9454, -0.5443],
							[1.9491, -0.3825, 0.7235]])

# create target tensors
target_tensor = torch.tensor([[0.2432, -0.1579, -1.0325],
							[-1.3464, 1.2442, 1.3847],
							[0.4528, 0.0876, 0.0499]])

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
