class RandomDataset(Dataset):
    def __init__(self, num_samples, num_features):
        self.num_samples = num_samples
        self.num_features = num_features
        self.data = torch.randn(num_samples, num_features)
        self.labels = torch.randint(0, 2, (num_samples,))

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

dataset = RandomDataset(1000, 20)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
