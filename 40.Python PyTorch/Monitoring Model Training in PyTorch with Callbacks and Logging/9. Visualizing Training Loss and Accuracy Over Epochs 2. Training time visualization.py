# Extract epoch times
epoch_times = [logs['epoch_time'] for logs in training_logs]

# Plot training time per epoch
plt.figure(figsize=(10, 5))
plt.bar(epochs, epoch_times, color='orange')
plt.title('Training Time per Epoch')
plt.xlabel('Epochs')
plt.ylabel('Time (seconds)')
plt.grid(axis='y')
plt.show()
