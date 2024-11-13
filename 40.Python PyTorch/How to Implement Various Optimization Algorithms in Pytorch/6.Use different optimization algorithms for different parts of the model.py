import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


# Define a neural network architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# Define the training dataset and data loader
transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
trainset = datasets.CIFAR10(
    root='./data', train=True, download=True, transform=transform)
trainloader = DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

# Move the model to the GPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
net = Net().to(device)

# Define the optimization algorithms
optimizers = [optim.SGD(net.parameters('fc3'), lr=0.001, momentum=0.9),
              optim.Adagrad(net.parameters('fc2'), lr=0.001),
              optim.Adam(net.parameters('fc1'), lr=0.001)]

# Train the neural network using different optimization algorithms
for epoch in range(10):
    running_loss = 0.0
    correct = 0
    total = 0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data
        # move data and target to the GPU
        inputs, labels = inputs.to(device), labels.to(device)
        for optimizer in optimizers:
            optimizer.zero_grad()
        outputs = net(inputs)

        EntropyLoss = nn.CrossEntropyLoss()(outputs, labels)
        fc1_loss = nn.L1Loss()(net.fc1.weight, torch.zeros_like(net.fc1.weight))
        fc2_loss = nn.L1Loss()(net.fc2.weight, torch.zeros_like(net.fc2.weight))
        total_loss = EntropyLoss + fc1_loss + fc2_loss
        total_loss.backward()

        for optimizer in optimizers:
            optimizer.step()
        running_loss += total_loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    print('Epoch: %d | Loss: %.3f | Accuracy: %.3f %%' %
          (epoch + 1, running_loss / len(trainloader), 100 * correct / total))
