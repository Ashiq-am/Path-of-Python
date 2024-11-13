# Import required library
import torch
import torch.nn as nn

# define input and target tensor
input_tens = torch.tensor([[0.4576, 0.6496, 0.6783],
						[0.4895, 0.9454, 0.5443],
						[0.9491, 0.3825, 0.7235]],
						requires_grad=True)

target_tens = torch.tensor([[0.2432, 0.1579, 0.0325],
							[0.3464, 0.2442, 0.3847],
							[0.4528, 0.0876, 0.0499], ])

# display input and target tensor
print('\n input tensor: \n', input_tens)
print('\n target tensor: \n', target_tens)

# define criterion to measure binary cross entropy
bce_loss = nn.BCELoss()

# compute the binary cross entropy
output = bce_loss(input_tens, target_tens)
output.backward()

# display result
print('\n Binary Cross Entropy Loss: \n', output)
