x_2 = torch.randn(2, 3)
y_2 = torch.randn(2, 5)

# second argument specifies which axis to concat along
z_2 = torch.cat([x_2, y_2], 1)
print(z_2)
