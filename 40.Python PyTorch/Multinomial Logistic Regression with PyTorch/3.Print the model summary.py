# Define the model
model = LogisticRegression(input_size=4, num_classes=3)

# Check for cuda
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
# Move the model to the device
model = model.to(device)
summary(model, input_size=(16,4))
