def objective(trial):
    # Hyperparameters to tune
    hidden_size = trial.suggest_int('hidden_size', 128, 512)
    learning_rate = trial.suggest_float('lr', 1e-4, 1e-1, log=True)

    # Load dataset
    transform = transforms.Compose([transforms.ToTensor()])
    train_loader = DataLoader(datasets.MNIST('./data', train=True, download=True, transform=transform), batch_size=32,
                              shuffle=True)

    model = Net(hidden_size)
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    criterion = nn.CrossEntropyLoss()

    # Training loop (1 epoch for simplicity)
    model.train()
    for epoch in range(1):
        for batch_idx, (data, target) in enumerate(train_loader):
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

    return loss.item()
