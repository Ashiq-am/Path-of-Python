import torch

# Generate a tensor of 10 numbers
data = torch.rand(10)

mean_tensor = data.mean()
std_tensor = data.std()

print(mean_tensor)
print(std_tensor)

mean = data.mean().item()
std = data.std().item()

print(mean)
print(std)
