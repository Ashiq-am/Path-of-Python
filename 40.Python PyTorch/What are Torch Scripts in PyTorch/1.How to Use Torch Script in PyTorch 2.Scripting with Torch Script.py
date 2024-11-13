import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 10)

    def forward(self, x):
        if x.sum() > 0:
            return self.fc(x)
        else:
            return torch.zeros_like(x)

# Script the model
scripted_model = torch.jit.script(SimpleModel())

# Save the scripted model
scripted_model.save("scripted_model.pt")
