import torch

# Initializing a linear layer with
# 2 independent features and 3 dependent features
linear_layer = torch.nn.Linear(2, 3)

# Initializing the weights with the
# normal initialization method
torch.nn.init.normal_(linear_layer.weight,
					mean=0, std=1)

# Displaying the initialized weights
print(linear_layer.weight)
