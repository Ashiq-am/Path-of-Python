def train(epoch, model, train_loader, optimizer, temp, cuda=True, hard=False):
    model.train()
    train_loss = 0
for batch_idx, (data, _) in enumerate(train_loader):
	data.to(device)
	optimizer.zero_grad()

	recon_batch, q_y = model(data, temp, hard)

	loss = loss_function(recon_batch, data, q_y)
	loss.backward()

	train_loss += loss.item() * len(data)
	optimizer.step()

	if batch_idx % 100 == 1:
		temp = np.maximum(temp * np.exp(-ANNEAL_RATE * batch_idx), temp_min)

	if batch_idx % 100 == 0:
		print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(epoch, batch_idx * len(data), len(train_loader.dataset),
				100. * batch_idx / len(train_loader),
				loss.item()))

print('====> Epoch: {} Average loss: {:.4f}'.format(epoch, train_loss / len(train_loader.dataset)))
