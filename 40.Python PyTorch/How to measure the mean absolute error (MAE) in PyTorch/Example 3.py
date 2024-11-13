# Import required libraries
import torch
import torch.nn as nn

# create input tensors
input_tensor = torch.tensor([[-0.3272, 1.7495, -0.6783],
							[0.4894, 0.4455, 1.5443],
							[0.3493, 1.3825, -0.7235], ])

# create target tensors
target_tensor = torch.tensor([[-0.4431, 1.7679, -1.0325],
							[-1.3464, 1.2442, 0.3847],
							[1.1528, 0.0876, 0.0499], ])

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
