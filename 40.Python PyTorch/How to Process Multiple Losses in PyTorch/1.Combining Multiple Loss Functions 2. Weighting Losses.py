import torch
import torch.nn as nn

model = nn.Linear(10, 2)
loss_fn1 = nn.CrossEntropyLoss()
loss_fn2 = nn.MSELoss()

# Example inputs and targets
inputs = torch.randn(3, 10)
target1 = torch.tensor([0, 1, 1])
target2 = torch.randn(3, 2)

# Forward pass
outputs = model(inputs)

# Calculate individual losses
loss1 = loss_fn1(outputs, target1)
loss2 = loss_fn2(outputs, target2)

print("Outputs:", outputs)
print("Loss1 (CrossEntropyLoss):", loss1.item())
print("Loss2 (MSELoss):", loss2.item())

# Define weights for each loss
weight1 = 0.7
weight2 = 0.3

# Combine losses with weights
total_loss = weight1 * loss1 + weight2 * loss2
total_loss.backward()

# Check gradients to ensure backpropagation worked
print("Gradients for model parameters:")
for name, param in model.named_parameters():
    if param.requires_grad:
        print(name, param.grad)
