class_sample_count = torch.tensor([(targets == t).sum() for t in torch.unique(targets)])
weight = 1. / class_sample_count.float()
samples_weight = torch.tensor([weight[int(t)] for t in targets])

sampler = WeightedRandomSampler(samples_weight, len(samples_weight))

train_loader = DataLoader(dataset, batch_size=64, sampler=sampler)

for batch_data, batch_target in train_loader:
    print(batch_data, batch_target)
