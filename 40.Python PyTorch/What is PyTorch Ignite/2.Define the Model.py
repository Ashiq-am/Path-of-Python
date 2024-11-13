# Define the model, optimizer, and loss function
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.8)
loss_fn = nn.CrossEntropyLoss()
