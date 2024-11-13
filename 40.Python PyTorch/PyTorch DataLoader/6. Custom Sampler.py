from torch.utils.data import Sampler
import random

class CustomSampler(Sampler):
    def __init__(self, data_source):
        self.data_source = data_source
        self.indices = list(range(len(data_source)))

    def __iter__(self):
        random.shuffle(self.indices)
        return iter(self.indices)

    def __len__(self):
        return len(self.indices)

custom_sampler = CustomSampler(dataset)
data_loader = DataLoader(dataset, batch_size=32, sampler=custom_sampler)
