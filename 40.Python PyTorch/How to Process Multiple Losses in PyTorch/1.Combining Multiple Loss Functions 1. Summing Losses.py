import torch
import torch.nn as nn

# Define your model
model = nn.Linear(10, 2)

# Define loss functions
loss_fn1 = nn.CrossEntropyLoss()
loss_fn2 = nn.MSELoss()

# Example inputs and targets
inputs = torch.randn(3, 10)
target1 = torch.tensor([0, 1, 1])  # Target for CrossEntropyLoss: class indices for 3 samples
target2 = torch.randn(3, 2)        # Target for MSELoss: same shape as model output

# Forward pass
outputs = model(inputs)

# Calculate individual losses
loss1 = loss_fn1(outputs, target1)
loss2 = loss_fn2(outputs, target2)

print("Outputs:", outputs)
print("Loss1 (CrossEntropyLoss):", loss1.item())
print("Loss2 (MSELoss):", loss2.item())

# Combine losses
total_loss = loss1 + loss2
print("Total Loss:", total_loss.item())

# Backward pass
total_loss.backward()

# Check gradients to ensure backpropagation worked
print("Gradients for model parameters:")
for name, param in model.named_parameters():
    if param.requires_grad:
        print(name, param.grad)
