import matplotlib.pyplot as plt

# Convert the tensor to channel-last format
image_np = image_tensor.permute(1, 2, 0).numpy()

# Display the image
plt.imshow(image_np)
plt.axis('off')  # Turn off axis labels
plt.show()
