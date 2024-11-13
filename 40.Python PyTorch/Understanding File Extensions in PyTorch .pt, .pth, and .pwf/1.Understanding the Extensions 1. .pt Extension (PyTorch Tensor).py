import torch
import torch.nn as nn

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 2)

    def forward(self, x):
        return self.fc(x)

model = SimpleModel()
torch.save(model.state_dict(), 'model.pt')
loaded_model = SimpleModel()
loaded_model.load_state_dict(torch.load('model.pt'))
loaded_model.eval()  # Set to evaluation mode
