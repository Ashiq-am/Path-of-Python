from torch.utils.data import DataLoader, RandomSampler,Dataset

datset=datasets.MNIST(root='./data',train=False,download=True,transform=t)
random_sampler = RandomSampler(dataset)
data_loader = DataLoader(dataset, batch_size=32, sampler=random_sampler)
