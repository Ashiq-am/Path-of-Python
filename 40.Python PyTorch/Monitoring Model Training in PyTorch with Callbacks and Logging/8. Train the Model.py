criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
callback = TrainingLogger(log_interval=10)
early_stopping_callback = EarlyStopping(patience=2)

train_model(model, dataloader, criterion, optimizer, epochs=5, callback=callback, early_stopping_callback=early_stopping_callback)
