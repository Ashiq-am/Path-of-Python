# File path to the dataset, replace this with your path
train_path = f'./maps/train'
test_path = f'./maps/val'


# Defining the train and test transforms
train_transform = torchvision.transforms.Compose([
	CustomTransform(),
	CustomAugmentation(),
])
test_transform = torchvision.transforms.Compose([
	CustomTransform(),
])


# Creating the train and test datasets
train_dataset = ImageDataset(train_path, transform=train_transform)
test_dataset = ImageDataset(test_path, transform=test_transform)


# Creating the train and test dataloaders
train_dataloader = torch.utils.data.DataLoader(
	dataset=train_dataset,
	batch_size=4,
	shuffle=True,
	num_workers=2
)
test_dataloader = torch.utils.data.DataLoader(
	dataset=test_dataset,
	batch_size=1,
	shuffle=False,
	num_workers=2
)

# Printing the length of the train and test dataloaders
print('Number of training batches:',len(train_dataloader))
print('Number of testing batches:',len(test_dataloader))
