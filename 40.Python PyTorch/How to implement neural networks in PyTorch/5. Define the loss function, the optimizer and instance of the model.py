# Create an instance of the model and move it to the device (CPU or GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # Get the device
model = Net().to(device) # Move the model to the device
print(model) # Print the model summary

# Define the loss function and the optimizer
criterion = nn.CrossEntropyLoss() # The cross entropy loss for multi-class classification
optimizer = optim.SGD(model.parameters(), lr=learning_rate) # The stochastic gradient descent optimizer

# Define a function to calculate the accuracy of the model
def accuracy(outputs, labels):
	# The accuracy is the percentage of correct predictions
	_, preds = torch.max(outputs, 1) # Get the predicted classes from the output logits
	return torch.sum(preds == labels).item() / len(labels) # Return the ratio of correct predictions
