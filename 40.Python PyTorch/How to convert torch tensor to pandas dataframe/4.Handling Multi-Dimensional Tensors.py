# Create a 3D tensor
tensor_3d = torch.randn(2, 3, 4)  # Example: 2 batches, 3 rows, 4 columns

# Reshape the tensor to 2D (flatten)
tensor_reshaped = tensor_3d.view(-1, 4)
print(tensor_reshaped)

# Convert the reshaped tensor to a Pandas DataFrame
df_3d = pd.DataFrame(tensor_reshaped.numpy())
print(df_3d)
