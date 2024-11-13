mlp = MLP() # Initialize MLP model
loss_function = nn.CrossEntropyLoss() # Cross-entropy loss function for classification
optimizer = torch.optim.Adam(mlp.parameters(), lr=1e-3) # Adam optimizer with learning rate 0.001
