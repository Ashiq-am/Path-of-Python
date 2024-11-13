import torch

# Initializing a linear layer with
# 2 independent features and 3 dependent features
linear_layer = torch.nn.Linear(2, 3)

# Initializing the weights with the Xavier initialization method
torch.nn.init.xavier_uniform_(linear_layer.weight)

# Displaying the initialized weights
print(linear_layer.weight)
