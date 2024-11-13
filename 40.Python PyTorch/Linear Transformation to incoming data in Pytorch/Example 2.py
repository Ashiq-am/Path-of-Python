# Python program to apply Linear transform
# to incoming data
# Step 1: Importing PyTorch
import torch

# Step 2: Define input data as torch tensor (float32)
data = torch.randn(3, 4)
print("Tensor before Transformation:\n", data)
print("dtype of Tensor:", data.dtype)
print("Size of Tensor:", data.size())

# Step 3: Define the in_features, out_features
in_features = 4
out_features = 2

# Step 4: Define a linear transformation
linear = torch.nn.Linear(in_features, out_features)

# Step 5: Apply the Linear transformation to the tensor
data_out = linear(data)
print("Transformed Tensor:\n", data_out)
print("Size of Transformed Tensor:", data_out.size())
