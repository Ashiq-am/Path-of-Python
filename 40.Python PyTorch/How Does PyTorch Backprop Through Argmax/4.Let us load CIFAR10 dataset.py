# Loading the dataset
from torchvision import transforms
from torchvision.datasets import CIFAR10
train_transforms = transforms.Compose([ transforms.ToTensor(), transforms.Normalize(mean=(0.4914, 0.4822, 0.4465), std=(0.2023, 0.1994, 0.2010))])
train_data = CIFAR10(root="./train/", train=True, download=True, transform=train_transforms)
trainloader = torch.utils.data.DataLoader( train_data,batch_size=16, shuffle=True)
