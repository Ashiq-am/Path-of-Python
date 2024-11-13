# import torch libraries
import torch

# creating a 1D tensor
tens = torch.tensor([4, 5, 0, -5, -4])

# Display tensor
print("\n\nInput Tensor: ", tens)

# compute the element-wise entropy of
# input tensor
entr = torch.special.entr(tens)

# Display result
print("\n\nComputed Entropy: ", entr)
