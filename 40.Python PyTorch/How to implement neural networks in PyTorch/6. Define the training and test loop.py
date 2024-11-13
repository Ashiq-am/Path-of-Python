# Define the training loop
def train(model, device, train_loader, criterion, optimizer, epoch):
	# Set the model to training mode
	model.train()
	# Initialize the running loss and accuracy
	running_loss = 0.0
	running_acc = 0.0
	# Loop over the batches of data
	for i, (inputs, labels) in enumerate(train_loader):
		# Move the inputs and labels to the device
		inputs = inputs.to(device)
		labels = labels.to(device)
		# Zero the parameter gradients
		optimizer.zero_grad()
		# Forward pass
		outputs = model(inputs) # Get the output logits from the model
		loss = criterion(outputs, labels) # Calculate the loss
		# Backward pass and optimize
		loss.backward() # Compute the gradients
		optimizer.step() # Update the parameters
		# Print the statistics
		running_loss += loss.item() # Accumulate the loss
		running_acc += accuracy(outputs, labels) # Accumulate the accuracy
		if (i + 1) % 200 == 0: # Print every 200 batches
			print(f'Epoch {epoch}, Batch {i + 1}, Loss: {running_loss / 200:.4f}, Accuracy: {running_acc / 200:.4f}')
			running_loss = 0.0
			running_acc = 0.0

# Define the test loop
def test(model, device, test_loader, criterion):
	# Set the model to evaluation mode
	model.eval()
	# Initialize the loss and accuracy
	test_loss = 0.0
	test_acc = 0.0
	# Loop over the batches of data
	with torch.no_grad(): # No need to track the gradients
		for inputs, labels in test_loader:
			# Move the inputs and labels to the device
			inputs = inputs.to(device)
			labels = labels.to(device)
			# Forward pass
			outputs = model(inputs) # Get the output logits from the model
			loss = criterion(outputs, labels) # Calculate the loss
			# Print the statistics
			test_loss += loss.item() # Accumulate the loss
			test_acc += accuracy(outputs, labels) # Accumulate the accuracy
	# Print the average loss and accuracy
	print(f'Test Loss: {test_loss / len(test_loader):.4f}, Test Accuracy: {test_acc / len(test_loader):.4f}')
