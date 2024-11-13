import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# Load a smaller subset of MNIST dataset
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

train_dataset = torchvision.datasets.MNIST(root='./data', train=True, transform=transform, download=True)
small_train_dataset = torch.utils.data.Subset(train_dataset, range(1000))  # Subset of first 1000 samples
train_loader = DataLoader(small_train_dataset, batch_size=64, shuffle=True)

# Initialize model, loss function, and optimizer
model = SimpleNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Initialize SummaryWriter for logging
writer = SummaryWriter('logs_small')

# Training loop
epochs = 5
for epoch in range(epochs):
    running_loss = 0.0
    correct = 0
    total = 0

    for i, (inputs, labels) in enumerate(train_loader):
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        # Calculate accuracy
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

        # Log loss
        writer.add_scalar('Loss/train', loss.item(), epoch * len(train_loader) + i)

    # Log accuracy
    accuracy = 100 * correct / total
    writer.add_scalar('Accuracy/train', accuracy, epoch)

    print(f'Epoch [{epoch + 1}/{epochs}], Loss: {running_loss / len(train_loader)}, Accuracy: {accuracy}%')

print('Finished Training')
writer.close()
