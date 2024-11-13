# import torch libraries
import torch

# creating a 2D tensor
tens = torch.tensor([[1, 2, -3],
					[0, -3, 2],
					[-2, 0, -3]])

# Display tensor
print("\n Input Tensor: \n", tens)

# compute the element-wise entropy of
# input tensor
entr = torch.special.entr(tens)

# Display result
print("\n Computed Entropy: \n", entr)
