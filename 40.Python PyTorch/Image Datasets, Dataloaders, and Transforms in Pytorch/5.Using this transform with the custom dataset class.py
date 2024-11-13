# Creating a dataset object with transforms
dataset = ImageDataset(data_path, transform=transform)

# Get the first splited image from the dataset
image, target = dataset[random_index]

# Plotting the image and target
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Image')
plt.subplot(1, 2, 2)
plt.imshow(target)
plt.title('Target')
plt.show()
