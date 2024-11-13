from torchvision import transforms

# Define a transformation pipeline
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Create an instance of the custom dataset with transformations
dataset = CustomNumpyDataset(numpy_list, transform=transform)

# Create a DataLoader
dataloader = DataLoader(dataset, batch_size=4, shuffle=True, num_workers=2)

# Iterate through the DataLoader
for batch in dataloader:
    print(batch.shape)
