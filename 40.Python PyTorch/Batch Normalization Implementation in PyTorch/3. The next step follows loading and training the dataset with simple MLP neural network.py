if __name__ == '__main__':
	# Set random seed for reproducibility
	torch.manual_seed(47)

	# Load the MNIST dataset
	transform = transforms.Compose([
		transforms.ToTensor()
	])
	train_data = MNIST(os.getcwd(), download=True, transform=transforms.ToTensor())
	train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
