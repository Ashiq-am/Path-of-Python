# Creating subplots
plt.figure(figsize=(12, 6))

# Subplot for Loss
plt.subplot(1, 2, 1)
plt.plot(first_model_trained.history['loss'], label='Training Loss')
plt.plot(first_model_trained.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss Over Epochs')
plt.legend()

# Subplot for Accuracy
plt.subplot(1, 2, 2)
plt.plot(first_model_trained.history['accuracy'], label='Training Accuracy')
plt.plot(
	first_model_trained.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy Over Epochs')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(loc='lower right')

# Adjusting layout to prevent overlap
plt.tight_layout()

# Displaying the plot
plt.show()
