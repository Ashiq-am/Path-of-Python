# Define the hyperparameters
batch_size = 64 # The number of samples per batch
num_epochs = 10 # The number of times to iterate over the whole dataset
learning_rate = 0.01 # The learning rate for the optimizer

# Define the transformation to apply to the images
transform = transforms.Compose([
	transforms.ToTensor(), # Convert the images to tensors
	transforms.Normalize((0.1307,), (0.3081,)) # Normalize the pixel values with mean and std
])
