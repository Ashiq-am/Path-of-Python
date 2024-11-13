# import the library
import torch

# check if CUDA is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# move tensor to device
x = torch.randn(10, 10).to(device)

class MyModel(torch.nn.Module):
	def __init__(self):
		super(MyModel, self).__init__()
		self.fc1 = torch.nn.Linear(10, 5)
		self.fc2 = torch.nn.Linear(5, 1)

	def forward(self, x):
		x = torch.nn.functional.relu(self.fc1(x))
		x = self.fc2(x)
		return x

# move model to device
model = MyModel().to(device)
