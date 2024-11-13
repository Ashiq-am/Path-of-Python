import matplotlib.pyplot as plt

# Extract loss and accuracy values from logs
loss_values = [logs['loss'] for logs in training_logs]
accuracy_values = [logs['accuracy'] for logs in training_logs]
epochs = range(1, len(loss_values) + 1)

# Plot loss over epochs
plt.figure(figsize=(10, 5))
plt.plot(epochs, loss_values, label='Loss', marker='o')
plt.title('Training Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()

# Plot accuracy over epochs
plt.figure(figsize=(10, 5))
plt.plot(epochs, accuracy_values, label='Accuracy', marker='o', color='green')
plt.title('Training Accuracy Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()
