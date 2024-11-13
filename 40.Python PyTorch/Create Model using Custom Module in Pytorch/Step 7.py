# Test the model
with torch.no_grad():
    y_true = []
    y_pred = []
    correct = 0
    total = 0
    for images, labels in test_loader:
        images = images.view(-1, 28 * 28)
        output = my_module(images)
        _, predicted = torch.max(output.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum()
        y_true += labels.tolist()
        y_pred += predicted.tolist()

    # Accuracy
    print('Accuracy: {} %'.format(100 * correct / total))

    # Generate the classification report
    report = classification_report(y_true, y_pred)
    print(report)
