# Train model
for epoch in range(5): # Train for 5 epochs
	running_loss = 0.0
	for inputs, labels in train_loader:
		optimizer.zero_grad() # Zero the gradients
		outputs = cnn_model(inputs) # Forward pass
		loss = loss_func(outputs, labels) # Calculate the loss
		loss.backward() # Backward pass
		optimizer.step() # Update weights


		running_loss += loss.item()
	print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader)}")
