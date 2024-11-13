# Define transformation to apply to the data
data_transform = transforms.Compose([
	transforms.ToTensor(), # Convert images to PyTorch tensors
	transforms.Normalize((0.5,), (0.5,)) # Normalize the pixel values to range [-1, 1]
])

# Download MNIST dataset and apply the transformation
train_dataset = torchvision.datasets.MNIST(root='./data', train=True, transform=data_transform, download=True)
test_dataset = torchvision.datasets.MNIST(root='./data', train=False, transform=data_transform, download=True)


# Define data loaders to load the data in batches during training and testing
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)
