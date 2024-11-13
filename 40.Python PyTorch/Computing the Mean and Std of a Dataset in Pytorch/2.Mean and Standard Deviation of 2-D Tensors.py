import torch

# Generate a tensor of shape (5,3)
data = torch.rand(5,3)

total_mean = data.mean()
total_std = data.std()

print(total_mean)
print(total_std)

# Mean and STD of columns
mean_col_wise = data.mean(axis = 0)
std_col_wise = data.std(axis = 0)

print(mean_col_wise)
print(std_col_wise)

# Mean and STD of rows
mean_row_wise = data.mean(axis = 1)
std_row_wise = data.std(axis = 1)

print(mean_row_wise)
print(std_row_wise)
