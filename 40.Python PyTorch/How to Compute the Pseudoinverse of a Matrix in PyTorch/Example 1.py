# import torch libraries
import torch

# creating a matrix or 4x3
inp = torch.tensor([[0.1150, -1.1121,
					0.2334, -0.2321],
					[1.2753, 1.0699,
					0.2335, 1.0177],
					[0.3942, -1.0498,
					-0.0486, 0.3240]])

# Display matrix
print("\n Input matrix: \n", inp)

# compute pseudoinverse of above defined matrix
output = torch.linalg.pinv(inp)

# Display result
print("\n After Compute pseudoinverse of matrix: \n",
	output)
