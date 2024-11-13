model = nn.Sequential(
	nn.Linear(30, 64), # Input layer with 30 features, hidden layer with 64 units
	nn.ReLU(),
	nn.Linear(64, 32), # Hidden layer with 32 units
	nn.ReLU(),
	nn.Linear(32, 1), # Output layer with 1 unit (for binary classification)
	nn.Sigmoid()
)
