import torch

# Initializing a linear layer with
# 2 independent features and 3 dependent features
linear_layer = torch.nn.Linear(2, 3)

# Initializing the weights with the Kaiming initialization method
torch.nn.init.kaiming_uniform_(linear_layer.weight,
							a=0, mode="fan_in",
							nonlinearity="relu")

# Displaying the initialized weights
print(linear_layer.weight)
