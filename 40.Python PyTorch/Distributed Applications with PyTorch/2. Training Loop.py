# Training loop
for epoch in range(10):
    ddp_model.train()
    for inputs, labels in dataloader:
        inputs, labels = inputs.to(rank), labels.to(rank)
        optimizer.zero_grad()
        outputs = ddp_model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
    print(f"Rank {rank}, Epoch {epoch}, Loss: {loss.item()}")

cleanup()
