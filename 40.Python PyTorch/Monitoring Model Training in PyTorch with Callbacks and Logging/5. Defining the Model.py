class SimpleNN(nn.Module):
    def __init__(self, input_size):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(input_size, 2)

    def forward(self, x):
        return self.fc(x)

model = SimpleNN(20)
