import torch
from torch.utils.data import DataLoader, WeightedRandomSampler, TensorDataset
import numpy as np

data = torch.randn(1000, 10)
targets = torch.cat((torch.zeros(900), torch.ones(100)))  # Imbalanced targets

# Create a dataset
train_dataset = TensorDataset(data, targets)

# Calculate weights for each class
class_sample_count = np.array([len(np.where(targets.numpy() == t)[0]) for t in np.unique(targets.numpy())])
weight = 1. / class_sample_count
samples_weight = np.array([weight[int(t)] for t in targets.numpy()])

samples_weight = torch.from_numpy(samples_weight)
sampler = WeightedRandomSampler(samples_weight, len(samples_weight))

train_loader = DataLoader(train_dataset, batch_size=64, sampler=sampler)

for batch_data, batch_target in train_loader:
    print(batch_data, batch_target)
