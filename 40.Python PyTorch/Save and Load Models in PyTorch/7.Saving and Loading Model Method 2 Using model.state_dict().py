# Saving the model
torch.save(cnn_model.state_dict(), 'cnn_model.pth')

# Loading the model
loaded_model = SimpleCNN()
loaded_model.load_state_dict(torch.load('cnn_model.pth'))
print(loaded_model)
