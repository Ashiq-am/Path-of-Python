# import torch module
import torch

# defining tensor
t = torch.tensor([[1, 2, 3, 4],
				[5, 6, 7, 8],
				[9, 10, 11, 12]])

# reshaping the tensor
print("Reshaping")
print(t.reshape(6, 2))

# resizing the tensor
print("\nResizing")
print(t.resize(2, 6))

# transposing the tensor
print("\nTransposing")
print(t.transpose(1, 0))
