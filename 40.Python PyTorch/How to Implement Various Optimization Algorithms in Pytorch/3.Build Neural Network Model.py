class Net(torch.nn.Module):
	def __init__(self):
		super(Net, self).__init__()
		self.fc1 = torch.nn.Linear(784, 128)
		self.fc2 = torch.nn.Linear(128, 128)
		self.fc3 = torch.nn.Linear(128, 10)

	def forward(self, x):
		x = x.view(-1, 784)
		x = torch.nn.functional.relu(self.fc1(x))
		x = torch.nn.functional.relu(self.fc2(x))
		x = torch.nn.functional.softmax(self.fc3(x), dim=1)
		return x

net = Net()
