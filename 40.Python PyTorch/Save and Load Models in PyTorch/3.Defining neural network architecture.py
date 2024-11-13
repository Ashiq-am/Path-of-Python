# Here we are adding convolution layer and fully connected layers in neural network
class SimpleCNN(nn.Module):
	def __init__(self):
		super(SimpleCNN, self).__init__()
		self.conv1_layer = nn.Conv2d(1, 16, kernel_size=3, padding=1)
		self.conv2_layer = nn.Conv2d(16, 32, kernel_size=3, padding=1)
		self.fc1_layer = nn.Linear(32 * 7 * 7, 128)
		self.fc2_layer = nn.Linear(128, 10)

	# Adding ReLU Activation function Max Pooling Layer
	def forward(self, inputs):
		new_input = torch.relu(self.conv1_layer(inputs))
		new_input = torch.max_pool2d(new_input, kernel_size=2, stride=2)
		new_input = torch.relu(self.conv2_layer(new_input))
		new_input = torch.max_pool2d(new_input, kernel_size=2, stride=2)
		new_input = new_input.view(-1, 32 * 7 * 7)
		new_input = torch.relu(self.fc1_layer(new_input))
		new_input = self.fc2_layer(new_input)
		return new_input


# Creating Model Instance
cnn_model = SimpleCNN()
