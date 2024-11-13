# Train and log results without optimizations
with SummaryWriter(log_dir='logs/original') as writer:
    for epoch in range(5):
        train(model, train_loader, criterion, optimizer, device)
        accuracy = validate(model, val_loader, criterion, device)
        print(f'Epoch {epoch + 1}, Accuracy: {accuracy}')
        log_results(writer, epoch, 0, accuracy)
