# Import required library
import torch

# define a tensor
tens = torch.tensor([-0.7345, 0.4347, -0.1237,
					1.3379, 0.2343])

# print the tensor
print("Original tensor:", tens)

# use troch.nn.Dropout() method with
# probability p=0.35
drop = torch.nn.Dropout(.35)
Output_tens = drop(tens)

# Display Output
print(" Output Tensor:", Output_tens)
