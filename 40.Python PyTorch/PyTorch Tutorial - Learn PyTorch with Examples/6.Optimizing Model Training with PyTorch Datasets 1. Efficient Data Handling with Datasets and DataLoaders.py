import torch
from torch.utils.data import Dataset, DataLoader

# Custom dataset example
class MyDataset(Dataset):
    def __init__(self):
        # Sample data and labels
        self.data = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        self.labels = torch.tensor([0, 1, 0])

    def __len__(self):
        # Return the size of the dataset
        return len(self.data)

    def __getitem__(self, idx):
        # Retrieve data and label by index
        return self.data[idx], self.labels[idx]

# Create dataset and dataloader
dataset = MyDataset()
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Iterate through data using DataLoader
for batch in dataloader:
    print("Batch Data:", batch[0])  # Input data
    print("Batch Labels:", batch[1])  # Corresponding labels
