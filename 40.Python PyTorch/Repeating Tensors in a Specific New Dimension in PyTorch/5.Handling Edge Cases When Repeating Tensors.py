x = torch.tensor([1, 2, 3])
x_repeated = x.repeat(1, 3)  # Repeat with size 1 on the first dimension

print("Repeated tensor with size 1:\n", x_repeated)
