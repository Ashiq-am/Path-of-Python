# Training loop
model.train()  # Set the model to training mode
optimizer.zero_grad()  # Zero the gradients
outputs = model(inputs)  # Forward pass
print("Model Outputs (before softmax):\n", outputs)

loss = criterion(outputs, labels)  # Compute the loss
print("Loss:", loss.item())

loss.backward()  # Backward pass (compute gradients)
optimizer.step()  # Update model parameters

# Updated model parameters for fc1 layer (optional)
print("\nUpdated fc1 weights:\n", model.fc1.weight)
print("Updated fc1 biases:\n", model.fc1.bias)
