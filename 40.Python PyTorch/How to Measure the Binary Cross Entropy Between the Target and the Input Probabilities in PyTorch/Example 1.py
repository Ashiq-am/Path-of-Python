# Import required library
import torch
import torch.nn as nn

# define input and target tensor
input_tens = torch.tensor(
	[0.4498, 0.9845, 0.4576, 0.3494, 0.2434],
	requires_grad=True)
target_tens = torch.tensor([0.2345, 0.5565,
							0.3468, 0.1444,
							0.3546])

# display input and target tensor
print('\n input tensor: ', input_tens)
print('\n target tensor: ', target_tens)

# define criterion to measure binary
# cross entropy
bce_loss = nn.BCELoss()

# compute the binary cross entropy
output = bce_loss(input_tens, target_tens)
output.backward()

# display result
print('\n Binary Cross Entropy Loss: ', output)
