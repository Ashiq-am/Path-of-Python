def euclidean_distance(x1, x2):
	return torch.sqrt(torch.sum((x1 - x2) ** 2, dim=1))
