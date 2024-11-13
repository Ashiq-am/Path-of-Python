# Define the training function
def train(model, X, Y):
    # Define the learning rate, number of iterations, and loss function
    learning_rate = 0.01
    n_iters = 100
    loss = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    # Loop through the specified number of iterations
    for epoch in range(n_iters):
        # Make predictions using the model
        y_predicted = model(X)

        # Calculate the loss
        l = loss(Y, y_predicted)

        # Backpropagate the loss to update the model parameters
        l.backward()
        optimizer.step()
        optimizer.zero_grad()

        # Print the current loss and weights every 10 epochs
        if epoch % 10 == 0:
            [w, b] = model.parameters()
            print(f'Rank {mp.current_process().name}: epoch {epoch + 1}: w = {w[0][0].item():.3f}, loss = {l:.3f}')
