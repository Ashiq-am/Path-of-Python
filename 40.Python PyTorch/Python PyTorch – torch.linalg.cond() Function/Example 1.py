# import the required library
import torch

# define a tensor (matrix)
M = torch.tensor([[-0.1345, -0.7437, 1.2377],
				[0.9337, 1.6473, 0.4346],
				[-1.6345, 0.9344, -0.2456]])

# display input tensor
print("\n Input Matrix M: \n", M)

# compute the condition number
Output = torch.linalg.cond(M)

# Display result
print("\n Condition Number: ", Output)
