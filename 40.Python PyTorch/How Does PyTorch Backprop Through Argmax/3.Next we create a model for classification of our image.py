# Creating our own LeNet5


class LeNet5(nn.Module):
	def __init__(self):
		super(LeNet5, self).__init__()
		self.conv1 = nn.Conv2d(3, 6, 5) # in channel , out channe, kernel
		self.relu1 = nn.ReLU()
		self.maxpool1 = nn.MaxPool2d((2, 2))

		self.conv2 = nn.Conv2d(6, 16, 5) # in channel , out channe, kernel
		self.relu2 = nn.ReLU()
		self.maxpool2 = nn.MaxPool2d((2, 2))

		self.fc1 = nn.Linear(16*5*5, 120)
		self.fc2 = nn.Linear(120, 84)
		self.fc3 = nn.Linear(84, 10)

	def forward(self, x):
		# x = F.max_pool2d(F.relu(self.conv1(x)),(2, 2))
		# x = F.max_pool2d(F.relu(self.conv2(x)), 2)
		x = self.conv1(x)
		x = self.relu1(x)
		x = self.maxpool1(x)

		x = self.conv2(x)
		x = self.relu2(x)
		x = self.maxpool2(x)

		x = x.view(-1, int(x.nelement() / x.shape[0]))
		x = F.relu(self.fc1(x))
		x = F.relu(self.fc2(x))
		x = self.fc3(x)

		x = torch.argmax(x, dim=1)

		return x


model = LeNet5()
