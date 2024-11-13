# Python program to normalize a tensor to
# 0 mean and 1 variance
# Step 1: Importing torch
import torch

# Step 2: creating a torch tensor
t = torch.tensor([1.,2.,3.,4.,5.])
print("Tensor before Normalize:\n", t)

# Step 3: Computing the mean, std and variance
mean, std, var = torch.mean(t), torch.std(t), torch.var(t)
print("Mean, Std and Var before Normalize:\n",
	mean, std, var)

# Step 4: Normalizing the tensor
t = (t-mean)/std
print("Tensor after Normalize:\n", t)

# Step 5: Again compute the mean, std and variance
# after Normalize
mean, std, var = torch.mean(t), torch.std(t), torch.var(t)
print("Mean, std and Var after normalize:\n",
	mean, std, var)
