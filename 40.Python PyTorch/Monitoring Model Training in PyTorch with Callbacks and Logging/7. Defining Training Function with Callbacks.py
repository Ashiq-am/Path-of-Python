def train_model(model, dataloader, criterion, optimizer, epochs, callback, early_stopping_callback=None):
    model.train()

    for epoch in range(epochs):
        callback.on_epoch_begin(epoch)
        running_loss = 0.0
        correct_predictions = 0
        total_predictions = 0

        for batch_idx, (inputs, labels) in enumerate(dataloader):
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct_predictions += (predicted == labels).sum().item()
            total_predictions += labels.size(0)

            callback.on_batch_end(batch_idx, logs={
                'loss': running_loss / (batch_idx + 1),
                'accuracy': correct_predictions / total_predictions
            })

        logs = {
            'loss': running_loss / len(dataloader),
            'accuracy': correct_predictions / total_predictions
        }
        callback.on_epoch_end(epoch, logs)

        if early_stopping_callback and early_stopping_callback.on_epoch_end(epoch, logs):
            break
