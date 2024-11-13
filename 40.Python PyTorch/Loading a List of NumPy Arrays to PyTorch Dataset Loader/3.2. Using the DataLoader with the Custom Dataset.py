from torch.utils.data import DataLoader

# Example list of NumPy arrays
numpy_list = [np.random.rand(3, 224, 224) for _ in range(100)]

# Create an instance of the custom dataset
dataset = CustomNumpyDataset(numpy_list)

# Create a DataLoader
dataloader = DataLoader(dataset, batch_size=4, shuffle=True, num_workers=2)

# Iterate through the DataLoader
for batch in dataloader:
    print(batch.shape)
