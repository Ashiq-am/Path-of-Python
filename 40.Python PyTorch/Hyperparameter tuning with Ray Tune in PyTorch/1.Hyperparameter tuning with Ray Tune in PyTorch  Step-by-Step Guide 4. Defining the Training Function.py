def train_cifar(config, checkpoint_dir=None):
    net = Net(config["l1"], config["l2"])
    device = "cuda" if torch.cuda.is_available() else "cpu"
    net.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=config["lr"], momentum=0.9)

    trainloader, testloader = load_data()

    for epoch in range(10):  # loop over the dataset multiple times
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            if i % 2000 == 1999:  # print every 2000 mini-batches
                print(f"[{epoch + 1}, {i + 1}] loss: {running_loss / 2000:.3f}")
                running_loss = 0.0

        # Validation loss
        val_loss = 0.0
        val_steps = 0
        for i, data in enumerate(testloader, 0):
            with torch.no_grad():
                inputs, labels = data
                inputs, labels = inputs.to(device), labels.to(device)
                outputs = net(inputs)
                loss = criterion(outputs, labels)
                val_loss += loss.cpu().numpy()
                val_steps += 1
        tune.report(loss=(val_loss / val_steps))

    print("Finished Training")
