# Training the model

N_EPOCHS = 2
for epoch in range(N_EPOCHS):
    epoch_loss = 0.0
for inputs, labels in trainloader:

    optimizer.zero_grad()

    outputs = model(inputs)

    loss = my_loss(outputs, labels.float())
    loss.backward()
    optimizer.step()
    epoch_loss += loss.item()

print("Epoch: {} Loss: {}".format(epoch,epoch_loss/len(trainloader)))
