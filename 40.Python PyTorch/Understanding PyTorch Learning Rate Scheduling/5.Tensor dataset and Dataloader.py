X_train_std_tensor = torch.FloatTensor(X_train_std)
Y_train_tensor = torch.FloatTensor(Y_train.values).view(-1, 1)

X_test_std_tensor = torch.FloatTensor(X_test_std)
Y_test_tensor = torch.FloatTensor(Y_test.values).view(-1, 1)

train_dataset = TensorDataset(X_train_std_tensor, Y_train_tensor)
train_loader = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True)
