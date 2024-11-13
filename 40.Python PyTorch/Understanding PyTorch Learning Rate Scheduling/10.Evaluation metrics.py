model.eval()
with torch.no_grad():
	test_outputs = model(X_test_std_tensor)
	test_predictions = (test_outputs >= 0.5).float() # Convert probabilities to binary predictions

	# Evaluation metrics (you can use appropriate metrics based on your problem)
	accuracy = (test_predictions == Y_test_tensor).float().mean().item()
	print(f'Test Accuracy: {accuracy}')
