test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)

model.eval()

with torch.no_grad():
    test_loss = 0
    for data, _ in test_loader:
        data = data.to(device)
        data = data.view(data.size(0), -1)
        recon_data = model(data)
        test_loss += criterion(recon_data, data).item()

    test_loss /= len(test_loader.dataset)
    print('Test Loss: {:.6f}'.format(test_loss))

    # Plot some input images and their reconstructions
    data, _ = next(iter(test_loader))
    data = data.to(device)
    data = data.view(data.size(0), -1)
    recon_data = model(data)

    fig, axes = plt.subplots(nrows=4, ncols=8, figsize=(16, 8))
    for i in range(0, 4, 2):
        for j in range(8):
            k = k = j if i == 0 else 8 + j
            axes[i, j].imshow(data[k].cpu().view(28, 28), cmap='gray')
            axes[i, j].set_title('Original')
            axes[i, j].set_axis_off()

            axes[i + 1, j].imshow(recon_data[k].cpu().view(28, 28), cmap='gray')
            axes[i + 1, j].set_title('Reconstruct')
            axes[i + 1, j].set_axis_off()

    fig.tight_layout()
    plt.show()
