import torch
from torch.utils.data import Dataset


class CustomNumpyDataset(Dataset):
    def __init__(self, numpy_list, transform=None):
        self.numpy_list = numpy_list
        self.transform = transform

    def __len__(self):
        return len(self.numpy_list)

    def __getitem__(self, idx):
        sample = self.numpy_list[idx]
        sample = torch.from_numpy(sample)

        if self.transform:
            sample = self.transform(sample)

        return sample
