class CustomNetwork(nn.Module):
    def __init__(self):
        super(CustomNetwork, self).__init__()
        self.fc1 = CustomLinear(28*28, 512)
        self.fc2 = CustomLinear(512, 256)
        self.fc3 = CustomLinear(256, 128)
        self.fc4 = CustomLinear(128, 64)
        self.fc5 = CustomLinear(64, 10)

    def forward(self, x):
        x = x.view(-1, 28*28)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = self.fc5(x)
        return x
