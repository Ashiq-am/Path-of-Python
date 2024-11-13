# Step 1: Define the Neural ODE Model
class ODEFunc(nn.Module):
    def __init__(self):
        super(ODEFunc, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 50),   # Input dimension is 2, hidden layer size is 50
            nn.Tanh(),          # Activation function (Tanh)
            nn.Linear(50, 2)    # Output dimension is 2
        )

    def forward(self, t, y):
        return self.net(y)  # Forward pass: returns the time derivative of the state
