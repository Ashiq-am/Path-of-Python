import torch
import torch.nn as nn

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 10)

    def forward(self, x):
        return self.fc(x)

# Instantiate the model and create a dummy input
model = SimpleModel()
dummy_input = torch.randn(1, 10)

# Trace the model
traced_model = torch.jit.trace(model, dummy_input)

# Save the traced model
traced_model.save("traced_model.pt")
