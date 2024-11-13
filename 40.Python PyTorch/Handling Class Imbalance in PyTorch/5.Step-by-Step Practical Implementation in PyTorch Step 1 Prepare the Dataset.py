import torch
from torch.utils.data import Dataset, DataLoader

class ImbalancedDataset(Dataset):
    def __init__(self, data, targets):
        self.data = data
        self.targets = targets

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.targets[idx]

# Example data
data = torch.randn(1000, 10)
targets = torch.cat((torch.zeros(900), torch.ones(100)))  # Imbalanced targets

dataset = ImbalancedDataset(data, targets)
