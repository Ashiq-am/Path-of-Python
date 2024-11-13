test_acc = 0
model.eval()

with torch.no_grad():
    # Iterating over the training dataset in batches
    for i, (images, labels) in enumerate(test_loader):
        images = images.to(device)
        y_true = labels.to(device)

        # Calculating outputs for the batch being iterated
        outputs = model(images)

        # Calculated prediction labels from models
        _, y_pred = torch.max(outputs.data, 1)

        # Comparing predicted and true labels
        test_acc += (y_pred == y_true).sum().item()

    print(f"Test set accuracy = {100 * test_acc / len(test_dataset)} %")
