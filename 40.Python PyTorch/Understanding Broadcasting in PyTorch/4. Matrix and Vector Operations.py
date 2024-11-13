matrix = torch.tensor([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
vector = torch.tensor([10, 20, 30])            # Shape (3,)

result = matrix + vector  # Broadcasting the vector to each row

print(result)
