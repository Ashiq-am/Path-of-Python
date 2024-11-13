# Define the transformation for QMNIST
transform_qmnist = transforms.Compose([
    transforms.Resize(224),
    transforms.Grayscale(num_output_channels=3),  # Convert to 3 channels
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])


# Download and create a DataLoader for the QMNIST test set
qmnist_test_dataset = QMNIST(root='./data', what='test', download=True, transform=transform_qmnist)
qmnist_test_loader = DataLoader(qmnist_test_dataset, batch_size=128, shuffle=False)
qmnist_test_labels = qmnist_test_dataset.targets

# Deploy the model on the QMNIST dataset
predictions_qmnist = []
with torch.no_grad():
    for images, _ in qmnist_test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        predictions_qmnist.extend(predicted.tolist())

# Display or use the results
print("Predictions for QMNIST test set:", predictions_qmnist)

correct_qmnist = sum(p == gt for p, gt in zip(predictions_qmnist, qmnist_test_labels))
total_qmnist = len(predictions_qmnist)
accuracy_qmnist = correct_qmnist / total_qmnist
