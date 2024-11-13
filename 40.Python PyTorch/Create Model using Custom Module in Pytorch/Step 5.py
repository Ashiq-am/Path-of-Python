train_dataset = datasets.MNIST(root='./data',
							train=True,
							download=True,
							transform=transform)
test_dataset = datasets.MNIST(root='./data',
							train=False,
							download=True,
							transform=transform)
