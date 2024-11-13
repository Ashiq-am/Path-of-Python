# Train the neural network using different optimization algorithms
for epoch in range(10):
	running_loss = 0.0
	correct = 0
	total = 0
	for i, data in enumerate(trainloader, 0):
		inputs, labels = data
		# move data and target to the GPU
		inputs, labels = inputs.to(device), labels.to(device)
		optimizer_sgd.zero_grad()
		optimizer_adam.zero_grad()
		optimizer_adagrad.zero_grad()
		optimizer_adadelta.zero_grad()
		outputs = net(inputs)
		loss = criterion(outputs, labels)
		loss.backward()
		optimizer_sgd.step()
		optimizer_adam.step()
		optimizer_adagrad.step()
		optimizer_adadelta.step()
		running_loss += loss.item()
		_, predicted = torch.max(outputs.data, 1)
		total += labels.size(0)
		correct += (predicted == labels).sum().item()

	print('Epoch: %d | Loss: %.3f | Accuracy: %.3f %%' %
		(epoch + 1, running_loss / len(trainloader), 100 * correct / total))
