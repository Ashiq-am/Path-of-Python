data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])  # Shape (2, 2)
scale = torch.tensor([0.1, 0.5])              # Shape (2,)

scaled_data = data * scale  # Broadcasting scale to shape (2, 2)

print(scaled_data)
