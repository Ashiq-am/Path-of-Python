# import the required library
import torch

# define a tensor (matrix)
M = torch.tensor([[[-0.1345, -0.7437, 1.2377],
				[0.9337, 1.6473, 0.4346],
				[-1.6345, 0.9344, -0.2456]],
				[[1.3343, -1.3456, 0.7373],
				[1.4334, 0.2473, 1.1333],
				[-1.5341, 1.5348, -1.4567]]])

# display input tensor
print(" Input Matrix M: \n", M)

# compute the condition number
Output = torch.linalg.cond(M)

# Display result
print("\n Condition Number: ", Output)
