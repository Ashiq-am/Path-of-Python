x = torch.randn(2, 3, 4)
print(x)

# reshape to 2 rows, 12 columns
print(x.view(2, 12))
