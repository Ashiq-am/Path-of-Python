# Train and test the model for the specified number of epochs
for epoch in range(1, num_epochs + 1):
	train(model, device, train_loader, criterion, optimizer, epoch) # Train the model
	test(model, device, test_loader, criterion) # Test the model

# Visualize some sample images and predictions
samples, labels = next(iter(test_loader)) # Get a batch of test data
samples = samples.to(device) # Move the samples to the device
outputs = model(samples) # Get the output logits from the model
_, preds = torch.max(outputs, 1) # Get the predicted classes from the output logits
samples = samples.cpu().numpy() # Move the samples back to CPU and convert to numpy array
fig, axes = plt.subplots(3, 3, figsize=(8, 8)) # Create a 3x3 grid of subplots
for i, ax in enumerate(axes.ravel()):
	ax.imshow(samples[i].squeeze(), cmap='gray') # Plot the image
	ax.set_title(f'Label: {labels[i]}, Prediction: {preds[i]}') # Set the title
	ax.axis('off') # Hide the axes
plt.tight_layout() # Adjust the spacing
plt.show() # Show the plot
