num_epochs = 3
batch_size = 128
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

for epoch in range(num_epochs):
    for batch_idx, (data, _) in enumerate(train_loader):

        data = data.to(device)
        data = data.view(data.size(0), -1)
        optimizer.zero_grad()
        recon_data = model(data)
        loss = criterion(recon_data, data)
        loss.backward()
        optimizer.step()

        if batch_idx % 100 == 0:
            print('Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(epoch,
                                                                     batch_idx * len(data),
                                                                     len(train_loader.dataset),
                                                                     100. * batch_idx / len(train_loader),
                                                                     loss.item()))
