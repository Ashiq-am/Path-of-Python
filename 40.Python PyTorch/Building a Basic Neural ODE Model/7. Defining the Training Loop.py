# Step 3: Define the Training Loop
def train_ode(model, optimizer, criterion, data):
    for epoch in range(100):                    # Number of epochs (iterations)
        optimizer.zero_grad()                   # Clear gradients from the previous step
        pred_y = odeint(model, data['y0'], data['t'])  # Solve ODE for current model state
        loss = criterion(pred_y.squeeze(), data['y_true'])  # Compute loss between predicted and true values
        loss.backward()                         # Backpropagate the error
        optimizer.step()                        # Update the model parameters
        if (epoch + 1) % 10 == 0:               # Print every 10 epochs
            print(f'Epoch {epoch+1}, Loss: {loss.item()}')
