import torch
import torch.nn as nn

class HybridModel(nn.Module):
    def __init__(self):
        super(HybridModel, self).__init__()
        self.fc1 = nn.Linear(10, 10)
        self.fc2 = nn.Linear(10, 10)

    def forward(self, x):
        x = self.fc1(x)
        if x.sum() > 0:
            x = self.fc2(x)
        return x

# Script the model
scripted_model = torch.jit.script(HybridModel())

# Save the model
scripted_model.save("hybrid_model.pt")
