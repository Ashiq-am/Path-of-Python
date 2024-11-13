class SwishActivation(nn.Module):
    def __init__(self):
        super(SwishActivation, self).__init__()

    def forward(self, x):
        sigmoid = 1 / (1 + torch.exp(-x))
        return x * sigmoid
