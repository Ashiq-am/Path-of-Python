# Import the required library
import torch

# define a tensor
tens = torch.tensor([[-0.1345, -0.7437, 1.2377],
					[0.9337, 1.6473, 0.4346],
					[-0.6345, 0.9344, -0.2456]])

# print the tensor
print("\n Original tensor: \n", tens)

# use troch.nn.Dropout() method with
# probability p=0.85
# perform this operation in-place by
# using inplace=True
drop = torch.nn.Dropout(.85)
Output_tens = drop(tens)

# Display Tensor
print("\n Output Tensor: \n", Output_tens)
