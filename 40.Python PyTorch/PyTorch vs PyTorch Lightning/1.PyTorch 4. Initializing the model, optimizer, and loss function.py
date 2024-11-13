# Initialize the model
model = NeuralNetwork()

# Define the optimizer and loss function
optimizer = optim.SGD(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()
