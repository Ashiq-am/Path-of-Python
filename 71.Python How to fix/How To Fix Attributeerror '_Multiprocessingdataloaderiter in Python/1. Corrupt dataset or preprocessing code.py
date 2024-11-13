import torch
from torch.utils.data import DataLoader, Dataset


class CorruptDataset(Dataset):
    def __len__(self):
        return 100

    def __getitem__(self, idx):
        if idx % 10 == 0:
            return None
        return torch.tensor(idx)


dataset = CorruptDataset()
dataloader = DataLoader(dataset, num_workers=4)

for batch in dataloader:
    print(batch)
