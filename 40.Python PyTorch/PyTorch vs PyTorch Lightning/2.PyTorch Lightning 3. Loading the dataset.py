# Load the MNIST dataset
train_dataset = MNIST(root='.', train=True, transform=ToTensor(), download=True)
val_dataset = MNIST(root='.', train=False, transform=ToTensor())

# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=64)
