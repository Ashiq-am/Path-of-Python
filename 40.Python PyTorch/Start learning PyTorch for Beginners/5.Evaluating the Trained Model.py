# Evaluate the model
with torch.no_grad():
	X_test_tensor = torch.FloatTensor(X_test)
	y_test_tensor = torch.LongTensor(y_test)
	outputs = model(X_test_tensor)
	_, predicted = torch.max(outputs, 1)
	accuracy = (predicted == y_test_tensor).sum().item() / len(y_test_tensor)
	print(f'Accuracy on the test set: {accuracy:.2f}')
