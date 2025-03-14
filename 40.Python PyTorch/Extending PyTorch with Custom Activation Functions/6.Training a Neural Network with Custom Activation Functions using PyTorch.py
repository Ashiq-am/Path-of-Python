# Import the necessary libraries
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt


# Define the Swish activation function
class SwishActivation(nn.Module):
    def __init__(self):
        super(SwishActivation, self).__init__()

    def forward(self, x):
        sigmoid = 1 / (1 + torch.exp(-x))
        return x * sigmoid

    # Define the neural network


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.activation = SwishActivation()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(-1, 784)
        x = self.activation(self.fc1(x))
        x = self.fc2(x)
        return x

    # Load the MNIST dataset


train_dataset = datasets.MNIST(root='./data',
                               train=True,
                               download=True,
                               transform=transforms.ToTensor())
train_loader = torch.utils.data.DataLoader(train_dataset,
                                           batch_size=128,
                                           shuffle=True)

# Initialize the neural network
model = Net()

# Define the loss function, optimizer, and learning rate
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Train the model
loss_list = []
for epoch in range(10):
    running_loss = 0.0
    for i, (inputs, labels) in enumerate(train_loader, 0):
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    loss_list.append(running_loss)
    print('Epoch %d loss: %.3f' % (epoch + 1, running_loss))

# Plot the loss vs iterations curve
plt.plot(loss_list)
plt.title('Loss vs Iterations')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.show()
