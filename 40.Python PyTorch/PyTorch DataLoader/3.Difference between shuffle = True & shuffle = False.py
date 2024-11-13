import torch
from torch.utils.data import DataLoader, TensorDataset

# Create a synthetic dataset of integers from 0 to 99
data = torch.arange(0, 100)
# Create dummy targets (just for the sake of having them)
targets = torch.zeros(100)

# Create a TensorDataset
dataset = TensorDataset(data, targets)

# DataLoader with shuffle=True
dataloader_shuffle = DataLoader(dataset, batch_size=10, shuffle=True)

# DataLoader with shuffle=False
dataloader_noshuffle = DataLoader(dataset, batch_size=10, shuffle=False)

# Function to print the first batch of the dataloader
def print_first_batch(dataloader, shuffle_status):
    for batch in dataloader:
        data, _ = batch
        print(f"First batch with shuffle={shuffle_status}: {data}")
        break  # We break the loop to print only the first batch

# Print the first batch of each DataLoader to compare
print_first_batch(dataloader_shuffle, shuffle_status=True)
print_first_batch(dataloader_noshuffle, shuffle_status=False)
