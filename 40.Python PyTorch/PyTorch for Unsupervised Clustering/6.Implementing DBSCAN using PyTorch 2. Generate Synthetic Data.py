# Generate synthetic data
X, _ = make_moons(n_samples=200, noise=0.05, random_state=0)
X = torch.tensor(X, dtype=torch.float)
