# Initialize centroids randomly
centroids = tensor_data[torch.randperm(tensor_data.size(0))[:4]]

# Define the number of iterations
num_iterations = 100

for _ in range(num_iterations):
	# Calculate distances from data points to centroids
	distances = torch.cdist(tensor_data, centroids)

	# Assign each data point to the closest centroid
	_, labels = torch.min(distances, dim=1)

	# Update centroids by taking the mean of data points assigned to each centroid
	for i in range(4):
		if torch.sum(labels == i) > 0:
			centroids[i] = torch.mean(tensor_data[labels == i], dim=0)
