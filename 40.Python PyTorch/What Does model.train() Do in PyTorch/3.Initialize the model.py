# Initialize the model, loss function, and optimizer
model = SimpleNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Dummy data
inputs = torch.randn(10, 10)  # 10 samples, each with 10 features
labels = torch.randint(0, 2, (10,))  # Random integer labels (0 or 1) for 10 samples
