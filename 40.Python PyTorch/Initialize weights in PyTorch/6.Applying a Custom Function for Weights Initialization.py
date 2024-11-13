import torch

# User defined function to initialize the weights
def custom_weights(m):
	torch.nn.init.uniform_(m.weight,
						-0.5, 0.5)

# Initializing a linear layer with
# 2 independent features and 3 dependent features
linear_layer = torch.nn.Linear(2, 3)

# Applying the user defined function to the layer
linear_layer.apply(custom_weights)

# Displaying the initialized weights
print(linear_layer.weight)
