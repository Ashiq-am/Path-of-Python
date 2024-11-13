# Training loop
for epoch in range(num_epochs):
	model.train()

	for inputs, targets in train_loader:
		outputs = model(inputs)
		targets = targets.unsqueeze(1).float() # Fix the shape of the targets
		loss = criterion(outputs, targets.view(-1, 1))


		optimizer.zero_grad()
		loss.backward()
		optimizer.step()

	# Adjust learning rate
	scheduler.step()

	# Print loss for monitoring
	print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item()}')
