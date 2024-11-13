import torch

# User defined Layer
class MyLayer(torch.nn.Module):

	# Overriding the constructor
	def __init__(self, independent, dependent):
		# Calling the super-class' constructor
		super(MyLayer, self).__init__()
		self.linear = torch.nn.Linear(independent,
									dependent)
		torch.nn.init.uniform_(self.linear.weight,
							-0.5, 0.5)

	def forward(self, x):
		return self.linear(x)


# Initializing a linear layer with
# 2 independent features and 3 dependent features
linear_layer = MyLayer(2, 3)

# Displaying the initialized weights
print(linear_layer.linear.weight)
