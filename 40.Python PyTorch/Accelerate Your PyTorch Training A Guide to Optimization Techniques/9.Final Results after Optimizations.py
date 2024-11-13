# The final results after optimizations
with SummaryWriter(log_dir='logs/optimized') as writer:
    for epoch in range(5):
        model.train()
        total_loss = 0
        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()

            # AMP: Scale the loss to prevent underflow
            with torch.cuda.amp.autocast():
                outputs = model(inputs)
                loss = criterion(outputs, labels)
            scaler.scale(loss).backward()

            # AMP: Unscales the gradients and performs optimization
            scaler.step(optimizer)
            scaler.update()

            total_loss += loss.item()

        accuracy = validate(model, val_loader, criterion, device)
        print(f'Epoch {epoch + 1}, Loss: {total_loss}, Accuracy: {accuracy}')
        log_results(writer, epoch, total_loss, accuracy)
