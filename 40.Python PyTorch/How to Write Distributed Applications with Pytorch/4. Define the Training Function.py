def train(rank, size):
    # Set environment variables for distributed setup
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'

    # Initialize the process group
    init_process(rank, size)

    # Create the model and wrap it in DDP
    model = SimpleModel()
    model = DDP(model)

    # Define optimizer and loss function
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    loss_fn = nn.MSELoss()

    # Training loop
    for epoch in range(10):
        # Generate fake data for demonstration
        inputs = torch.randn(20, 10)
        targets = torch.randn(20, 1)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_fn(outputs, targets)
        loss.backward()
        optimizer.step()

        if rank == 0:  # Print loss from the main process
            print(f'Epoch {epoch}, Loss: {loss.item()}')
