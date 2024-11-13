import torch
import torch.nn as nn

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 2)

    def forward(self, x):
        return self.fc(x)

# Initialize the model
model = SimpleModel()

# Save model weights
torch.save(model.state_dict(), 'model_weights.pth')

# Load model weights
loaded_model = SimpleModel()
loaded_model.load_state_dict(torch.load('model_weights.pth'))
loaded_model.eval()  # Set to evaluation mode
