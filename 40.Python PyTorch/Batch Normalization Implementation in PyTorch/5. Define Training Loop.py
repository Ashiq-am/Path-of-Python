start_time = time.time()

# Training loop
for epoch in range(3): # Iterate over 3 epochs
	print(f'Starting epoch {epoch + 1}')
	running_loss = 0.0
	for i, data in enumerate(train_loader, 0):
		inputs, labels = data
		optimizer.zero_grad() # Zero the gradients
		outputs = mlp(inputs.view(inputs.shape[0], -1)) # Flatten the input for MLP and forward pass
		loss = loss_function(outputs, labels) # Compute the loss
		loss.backward() # Backpropagation
		optimizer.step() # Optimizer step to update parameters

		running_loss += loss.item()
		if i % 100 == 99: # Print every 100 mini-batches
			print(f'Epoch {epoch + 1}, Mini-batch {i + 1}, Loss: {running_loss / 100}')
			running_loss = 0.0
print('Training finished')

end_time = time.time() # Record end time
print('Training process has been completed. ')
training_time = end_time - start_time

print('Training time:', str(datetime.timedelta(seconds=training_time))) # for calculating the training time in minutes and seconds format
