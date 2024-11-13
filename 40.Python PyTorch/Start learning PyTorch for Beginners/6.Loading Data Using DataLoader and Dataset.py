import torch
from torch.utils.data import DataLoader, Dataset


# Custom Dataset class
class CustomDataset(Dataset):
	def __init__(self, data, targets):
		self.data = data
		self.targets = targets

	def __len__(self):
		return len(self.data)

	def __getitem__(self, idx):
		return self.data[idx], self.targets[idx]


# Example data
data = torch.randn(100, 3, 32, 32) # Example image data
targets = torch.randint(0, 10, (100,)) # Example target labels


# Create custom dataset
custom_dataset = CustomDataset(data, targets)


# Create DataLoader
batch_size = 32
shuffle = True
num_workers = 4
data_loader = DataLoader(custom_dataset, batch_size=batch_size,
						shuffle=shuffle, num_workers=num_workers)


# Iterate over batches
for batch_idx, (inputs, targets) in enumerate(data_loader):
	print(
		f"Batch {batch_idx+1}: Inputs shape: {inputs.shape}, Targets shape: {targets.shape}")
