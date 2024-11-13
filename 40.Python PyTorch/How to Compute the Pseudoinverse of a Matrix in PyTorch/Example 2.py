# import torch libraries
import torch

# creating a batch matrix
inp = torch.tensor([[[1.1232, 0.2341, 0.1323],
					[-1.0562, 0.1897, 0.1276]],
					[[-1.0200, -1.1121, 1.0321],
					[1.0887, -1.0564, 0.1798]]])

# Display batch of matrix
print("\n Batch of matrix: \n", inp)

# compute pseudoinverse of above defined matrix
output = torch.linalg.pinv(inp)

# Display result
print("\n After Compute pseudoinverse: \n",
	output)
