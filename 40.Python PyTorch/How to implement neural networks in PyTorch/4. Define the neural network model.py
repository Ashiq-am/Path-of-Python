# Define the neural network model
class Net(nn.Module):
	def __init__(self):
		super(Net, self).__init__()
		# The network has two fully connected layers
		self.fc1 = nn.Linear(28*28, 512) # The first layer takes the flattened image as input and outputs 512 features
		self.fc2 = nn.Linear(512, 10) # The second layer takes the 512 features as input and outputs 10 classes

	def forward(self, x):
		# The forward pass of the network
		x = x.view(-1, 28*28) # Flatten the image into a vector
		x = F.relu(self.fc1(x)) # Apply the ReLU activation function to the first layer
		x = self.fc2(x) # Apply the second layer
		return x # Return the output logits
