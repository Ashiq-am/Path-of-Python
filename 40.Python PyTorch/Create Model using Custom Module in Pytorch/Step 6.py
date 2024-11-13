for epoch in range(20):
	for i, (images, labels) in enumerate(train_loader):
		images = images.view(-1, 28*28)
		optimizer.zero_grad()
		output = my_module(images)
		loss = criterion(output, labels)
		loss.backward()
		optimizer.step()
	print('Epoch',epoch,' Loss -->',loss)
