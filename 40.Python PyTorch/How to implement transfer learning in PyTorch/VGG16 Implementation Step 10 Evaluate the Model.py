test_dataset = MNIST(root='./data', train=False, download=True, transform=transform_test)
test_loader = DataLoader(test_dataset, batch_size=128, shuffle=False)  # Don't shuffle test data

# Initialize variables for tracking performance
test_losses = []
correct = 0
total = 0

# Loop through epochs for testing
for epoch in range(num_epochs):
    with torch.no_grad():
        running_loss = 0.0

        # Evaluate the model on the test set
        for images, labels in test_loader:
            # Forward pass (no need for gradients during testing)
            outputs = model(images)

            # Calculate loss (assuming your loss function is defined)
            loss = criterion(outputs, labels)

            # Update running loss
            running_loss += loss.item()

            # Calculate accuracy
            _, predicted = torch.max(outputs.data, 1)  # Get the index of the maximum value
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        # Calculate average loss for the epoch
        test_loss = running_loss / len(test_loader.dataset)
        test_losses.append(test_loss)

    # Print epoch-wise performance (optional)
    print(f'Epoch {epoch+1} - Test Loss: {test_loss:.4f}')

# Calculate and print overall test accuracy
test_accuracy = correct / total
print(f'Accuracy of the model on the test set: {test_accuracy:.4f}')
