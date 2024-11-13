from torch.utils.data import DataLoader
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load the MNIST dataset
mnist_dataset_train = datasets.MNIST(
	root='./data', train=True, download=True, transform=transforms.ToTensor())
# Load the MNIST dataset
mnist_dataset_test = datasets.MNIST(
	root='./data', train=True, download=True, transform=transforms.ToTensor())


batch_size = 128
train_loader = torch.utils.data.DataLoader(
	mnist_dataset_train, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(
	mnist_dataset_test, batch_size=batch_size, shuffle=True)
