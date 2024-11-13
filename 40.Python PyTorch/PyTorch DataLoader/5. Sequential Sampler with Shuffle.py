from torch.utils.data import SequentialSampler

sequential_sampler = SequentialSampler(dataset)
data_loader = DataLoader(dataset, batch_size=32, sampler=sequential_sampler)
