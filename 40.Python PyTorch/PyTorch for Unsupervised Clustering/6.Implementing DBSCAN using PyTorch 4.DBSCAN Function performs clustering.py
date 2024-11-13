def dbscan(X, eps, min_samples):
    n_samples = X.shape[0]
    labels = torch.zeros(n_samples, dtype=torch.int)

    # Initialize cluster label and visited flags
    cluster_label = 0
    visited = torch.zeros(n_samples, dtype=torch.bool)

    # Iterate over each point
    for i in range(n_samples):
        if visited[i]:
            continue
        visited[i] = True

        # Find neighbors
        neighbors = torch.nonzero(euclidean_distance(X[i], X) < eps).squeeze()

        if neighbors.shape[0] < min_samples:
            # Label as noise
            labels[i] = 0
        else:
            # Expand cluster
            cluster_label += 1
            labels[i] = cluster_label
            expand_cluster(X, labels, visited, neighbors, cluster_label, eps, min_samples)

    return labels
