# Features are 3 random normal variables
features = torch.randn((1, 3))

# Define the size of each layer in our network

# Number of input units, must match number of input features
n_input = features.shape[1]
n_hidden = 2			 # Number of hidden units
n_output = 1			 # Number of output units

# Weights for inputs to hidden layer
W1 = torch.randn(n_input, n_hidden)

# Weights for hidden layer to output layer
W2 = torch.randn(n_hidden, n_output)

# and bias terms for hidden and output layers
B1 = torch.randn((1, n_hidden))
B2 = torch.randn((1, n_output))
