# importing torch
import torch

# create tensor
t1 = torch.tensor([[1, 2, 3],
				[5, 6, 7],
				[9, 10, 11]])

# printing the tensor
print(t1)

print()

# shuffle rows - first position to third position and
# third position to first position
print(t1[torch.tensor([2, 1, 0])][:, torch.tensor([0, 1, 2])])
