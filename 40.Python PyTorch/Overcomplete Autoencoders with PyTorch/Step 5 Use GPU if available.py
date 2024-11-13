device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print('Device is',device)
model.load_state_dict(torch.load(PATH))
model.to(device)

# Move the model to the GPU if available
model.to(device)
summary(model, (1,784))
