from torch.utils.data import DataLoader

if __name__ == '__main__':
    loader = DataLoader(dataset, num_workers=0)
    for data in loader:
        # process data
