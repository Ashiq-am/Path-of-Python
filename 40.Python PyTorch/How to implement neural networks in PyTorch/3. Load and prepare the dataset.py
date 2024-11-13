# Load the MNIST dataset from the web
train_dataset = datasets.MNIST(root='.', train=True, download=True, transform=transform) # The training set
test_dataset = datasets.MNIST(root='.', train=False, download=True, transform=transform) # The test set

# Create the data loaders for batching and shuffling the data
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True) # The training loader
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False) # The test loader
