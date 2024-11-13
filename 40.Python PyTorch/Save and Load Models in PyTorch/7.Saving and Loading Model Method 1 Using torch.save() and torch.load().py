# Save the model
torch.save(cnn_model.state_dict(), 'cnn_model.pth')

# Load the model
loaded_model = SimpleCNN()
loaded_model.load_state_dict(torch.load('cnn_model.pth'))

# Set the model to evaluation mode
loaded_model.eval()
