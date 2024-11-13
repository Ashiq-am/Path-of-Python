# Defining augmented and non-augmented transforms
aug_transform = torchvision.transforms.Compose([
	# Replace with the transform object
	CustomTransform(),
	CustomAugmentation(),
])
nonaug_transform = torchvision.transforms.Compose([
	# Replace with the transform object
	CustomTransform(),
])

# Creating a dataset object with augmented and non-augmented transforms
aug_dataset = ImageDataset(data_path, transform=aug_transform)
nonaug_dataset = ImageDataset(data_path, transform=nonaug_transform)

# Displaying a non augmented images from the dataset and its augmented version
image, target = nonaug_dataset[random_index]

# Creating a plot
plt.figure(figsize=(10, 10))
# Adding the non augmented image
plt.subplot(2, 2, 1)
plt.imshow(target)
plt.title('Non augmented image')

# Adding the augmented images
for i in range(2, 5):
	image, target1 = aug_dataset[random_index]
	plt.subplot(2, 2, i)
	plt.imshow(target1)
	plt.title('Augmented image')

# Displaying the plot
plt.show()
