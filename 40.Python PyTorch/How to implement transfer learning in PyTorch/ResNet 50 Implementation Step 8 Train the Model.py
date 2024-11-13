# Enable gradient computation for the last few layers
for param in model.resnet.layer4.parameters():
    param.requires_grad = True

# Train the model
model.train()
