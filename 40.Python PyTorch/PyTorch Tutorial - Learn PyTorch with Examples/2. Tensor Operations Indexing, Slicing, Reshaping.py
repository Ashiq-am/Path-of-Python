import torch

# Create a 3x2 tensor
tensor = torch.tensor([[1, 2], [3, 4], [5, 6]])

# 1. Indexing: Access the element at row 1, column 0
element = tensor[1, 0]
print(f"Indexed Element (Row 1, Column 0): {element}")  # Outputs: 3

# 2. Slicing: Extract the first two rows
slice_tensor = tensor[:2, :]
print(f"Sliced Tensor (First two rows): \n{slice_tensor}")

# 3. Reshaping: Reshape the tensor to a 2x3 tensor
reshaped_tensor = tensor.view(2, 3)
print(f"Reshaped Tensor (2x3): \n{reshaped_tensor}")
