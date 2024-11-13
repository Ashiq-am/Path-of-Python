class MyModule(nn.Module):

    # Initialize the parameter
    def __init__(self, num_inputs, num_outputs, hidden_size):
        super(MyModule, self).__init__()
        self.linear1 = nn.Linear(num_inputs, hidden_size)
        self.linear2 = nn.Linear(hidden_size, num_outputs)

    # Forward pass
    def forward(self, input):
        lin = self.linear1(input)
        output = nn.functional.relu(lin)
        pred = self.linear2(output)
        return pred
