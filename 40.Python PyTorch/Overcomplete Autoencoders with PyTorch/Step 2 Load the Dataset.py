train_dataset = datasets.MNIST(root='data/',
							train=True,
							transform=transforms.ToTensor(),
							download=True)
test_dataset = datasets.MNIST(root='data/',
							train=False,
							transform=transforms.ToTensor(),
							download=True)
