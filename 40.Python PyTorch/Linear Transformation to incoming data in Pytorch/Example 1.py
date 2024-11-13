# Python program to apply Linear transform
# to incoming data
# Step 1: Importing PyTorch
import torch

# Step 2: Define incoming data as torch
# tensor (float32)
data = torch.tensor([23., 12., 33., 4.01, -65.])
print("Data before Transformation:\n", data)
print("dtype of Data:", data.dtype)
print("Size of Data:", data.size())

# Step 3: Define the in_features, out_features
in_features = 5
out_features = 3

# Step 4: Define a linear transformation
linear = torch.nn.Linear(in_features, out_features)

# Step 5: Apply the Linear transformation to
# the tensor
data_out = linear(data)
print("Data after Transformation:\n", data_out)
print("Size of Data after Transformation:", data_out.size())
