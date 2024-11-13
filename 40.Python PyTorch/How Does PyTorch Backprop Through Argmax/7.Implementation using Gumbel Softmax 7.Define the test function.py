def test(epoch, model, test_loader, temp, cuda=True, hard=False):
    model.eval()
    test_loss = 0

for i, (data, _) in enumerate(test_loader):
	data.to(device)

	recon_batch, qy = model(data, temp, hard)
	test_loss += loss_function(recon_batch, data, qy).item() * len(data)

	if i % 100 == 1:
		temp = np.maximum(temp * np.exp(-ANNEAL_RATE * i), temp_min)

	if i == 0:
		n = min(data.size(0), 8)
		comparison = torch.cat([data[:n],recon_batch.view(128, 1, 28, 28)[:n]])
		save_image(comparison.data.to(device),f"./reconstruction_{epoch:03d}.png", nrow=n)

test_loss /= len(test_loader.dataset)
print('====> Test set loss: {:.4f}'.format(test_loss))
