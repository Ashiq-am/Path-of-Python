# Define training parameters
num_epochs = 1000

# Train the model
for epoch in range(num_epochs):
	for i, (inputs, labels) in enumerate(train_loader):
		# Move inputs and labels to the device
		inputs = inputs.to(device)
		labels = labels.to(device)

		# Forward pass
		outputs = model(inputs)
		loss = criterion(outputs, labels)

		# Backward and optimize
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()

	# Print training loss for each epoch
	if (epoch+1)%100 == 0:
		print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))
