from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# DataLoader with shuffle = True
train_loader = DataLoader(datasets.MNIST('data', train=True, download=True,
                           transform=transforms.Compose([
                               transforms.ToTensor(),
                               transforms.Normalize((0.1307,), (0.3081,))
                           ])),
                           batch_size=64, shuffle=True)
