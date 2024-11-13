def train_cifar(config, checkpoint_dir=None):
    net = Net(config["l1"], config["l2"])
    device = "cuda" if torch.cuda.is_available() else "cpu"
    net.to(device)

    if checkpoint_dir:
        checkpoint = torch.load(os.path.join(checkpoint_dir, "checkpoint"))
        net.load_state_dict(checkpoint["net"])
        optimizer.load_state_dict(checkpoint["optimizer"])

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=config["lr"], momentum=0.9)

    trainloader, testloader = load_data()

    for epoch in range(10):
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
            if i % 2000 == 1999:
                print(f"[{epoch + 1}, {i + 1}] loss: {running_loss / 2000:.3f}")
                running_loss = 0.0

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

        if epoch % 5 == 4:
            with tune.checkpoint_dir(epoch) as checkpoint_dir:
                path = os.path.join(checkpoint_dir, "checkpoint")
                torch.save({
                    "net": net.state_dict(),
                    "optimizer": optimizer.state_dict()
                }, path)

    print("Finished Training")
