# Generate synthetic data
data, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Convert data to PyTorch tensor
tensor_data = torch.from_numpy(data).float()
