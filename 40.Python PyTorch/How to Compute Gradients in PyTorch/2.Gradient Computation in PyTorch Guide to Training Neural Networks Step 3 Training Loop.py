# Number of epochs
epochs = 5000

for epoch in range(epochs):
    # Forward pass: Compute predicted y by passing x to the model
    pred_y = net(X)

    # Compute and print loss
    loss = criterion(pred_y, y)
    if (epoch+1) % 500 == 0:
        print(f'Epoch {epoch+1}, Loss: {loss.item()}')

    # Zero gradients, perform a backward pass, and update the weights.
    optimizer.zero_grad()  # Clear gradients for next train
    loss.backward()        # Backpropagation, compute gradients
    optimizer.step()       # Apply gradients
