import torch
from torch.utils.data import DataLoader, Dataset


class SimpleDataset(Dataset):
    def __len__(self):
        return 100

    def __getitem__(self, idx):
        return torch.tensor(idx)


dataset = SimpleDataset()
dataloader = DataLoader(dataset, num_workers=4)

iterator = iter(dataloader)
try:
    next(iterator)
except AttributeError as e:
    print(f"Caught an error in this code: {e}")
