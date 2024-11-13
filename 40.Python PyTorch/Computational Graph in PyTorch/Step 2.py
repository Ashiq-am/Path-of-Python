# Define a neural network architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3)
        self.pool = nn.MaxPool2d(3, 2)
        self.fc1 = nn.Linear(238, 120)
        self.fc2 = nn.Linear(120, 1)
        self.fc3 = nn.Sigmoid()

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(-1, 238)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        return x


# Move the model to the GPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
net = Net().to(device)
