class RegressionModel(nn.Module):
    def __init__(self):
        super(RegressionModel, self).__init__()
        self.linear = nn.Linear(5, 1)  # Predicts a single continuous value

    def forward(self, x):
        return self.linear(x)


model = RegressionModel()
input_data = torch.randn(1, 5)
output = model(input_data)
print(output)  # Single continuous output
