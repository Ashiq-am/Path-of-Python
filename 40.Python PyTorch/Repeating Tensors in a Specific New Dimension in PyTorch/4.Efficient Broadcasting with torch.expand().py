tensor = torch.tensor([1, 2, 3])

# Expand the tensor to a 4x3 matrix without duplicating the data
expanded_tensor = tensor.unsqueeze(0).expand(4, 3)
print(expanded_tensor)
