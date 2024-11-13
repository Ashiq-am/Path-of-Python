# Evaluate the model on the validation set
with torch.no_grad():
	correct = 0
	total = 0
	for inputs, labels in val_loader:
		# Move inputs and labels to the device
		inputs = inputs.to(device)
		labels = labels.to(device)

		# Compute the model's predictions
		outputs = model(inputs)
		_, predicted = torch.max(outputs.data, 1)

		# Compute the accuracy
		total += labels.size(0)
		correct += (predicted == labels).sum().item()

	print('Validation Accuracy: {:.2f}%'.format(100 * correct / total))
