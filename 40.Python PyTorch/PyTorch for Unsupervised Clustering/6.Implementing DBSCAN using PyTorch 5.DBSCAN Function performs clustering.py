def expand_cluster(X, labels, visited, neighbors, cluster_label, eps, min_samples):
	i = 0
	while i < neighbors.shape[0]:
		neighbor_index = neighbors[i].item()
		if not visited[neighbor_index]:
			visited[neighbor_index] = True
			neighbor_neighbors = torch.nonzero(euclidean_distance(X[neighbor_index], X) < eps).squeeze()
			if neighbor_neighbors.shape[0] >= min_samples:
				neighbors = torch.cat((neighbors, neighbor_neighbors))
		if labels[neighbor_index] == 0:
			labels[neighbor_index] = cluster_label
		i += 1
