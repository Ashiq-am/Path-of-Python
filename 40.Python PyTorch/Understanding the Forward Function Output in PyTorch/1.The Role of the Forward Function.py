import torch
import torch.nn as nn


class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(10, 2)

    def forward(self, x):
        return self.linear(x)


# Creating an instance of the model and performing a forward pass
model = SimpleModel()
input_data = torch.randn(1, 10)
output = model(input_data)
print(output)
