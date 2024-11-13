# Define your neural network architecture with batch normalization
class MLP(nn.Module):
	def __init__(self):
		super().__init__()
		self.layers = nn.Sequential(
			nn.Flatten(),				 # Flatten the input image tensor
			nn.Linear(28 * 28, 64),		 # Fully connected layer from 28*28 to 64 neurons
			nn.BatchNorm1d(64),			 # Batch normalization for stability and faster convergence
			nn.ReLU(),					 # ReLU activation function
			nn.Linear(64, 32),			 # Fully connected layer from 64 to 32 neurons
			nn.BatchNorm1d(32),			 # Batch normalization for stability and faster convergence
			nn.ReLU(),					 # ReLU activation function
			nn.Linear(32, 10)			 # Fully connected layer from 32 to 10 neurons (for MNIST classes)
		)

	def forward(self, x):
		return self.layers(x)
