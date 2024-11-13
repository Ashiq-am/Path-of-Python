import torch
from torch.utils.data import Dataset, DataLoader


# Define custom dataset class by subclassing torch.utils.data.Dataset
class CustomDataset(Dataset):
    def __init__(self, data, targets):
        self.data = data
        self.targets = targets

    def __len__(self):
        # Return the total number of samples in the dataset
        return len(self.data)

    def __getitem__(self, index):
        # Retrieve and return a sample and its corresponding target based on the given index
        sample = self.data[index]
        target = self.targets[index]
        return sample, target


# Example data and targets
data = torch.tensor([[1, 2], [3, 4], [5, 6], [7, 8]])
targets = torch.tensor([0, 1, 0, 1])

# Create instance of the custom dataset
custom_dataset = CustomDataset(data, targets)

# Create a data loader to iterate over the dataset in batches
batch_size = 2
data_loader = DataLoader(custom_dataset, batch_size=batch_size, shuffle=True)

# Iterate over the data loader to access batches of data
for batch_idx, (samples, targets) in enumerate(data_loader):
    print(f"Batch {batch_idx}:")
    print("Samples:", samples)
    print("Targets:", targets)
