import torch


class Model (torch.nn.Module) :
    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(1, 1)


    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred
