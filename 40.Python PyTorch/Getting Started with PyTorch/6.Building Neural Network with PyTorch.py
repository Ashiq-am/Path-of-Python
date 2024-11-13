# importing torch
import torch

# training input(X) and output(y)
X = torch.Tensor([[1], [2], [3],
                  [4], [5], [6]])
y = torch.Tensor([[5], [10], [15],
                  [20], [25], [30]])


class Model(torch.nn.Module):

    # defining layer
    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    # implimenting forward pass
    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred


model = torch.nn.Linear(1, 1)

# defining loss function and optimizer
loss_fn = torch.nn.L1Loss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(1000):
    # predicting y using initial weigths
    y_pred = model(X.requires_grad_())

    # loss calculation
    loss = loss_fn(y_pred, y)

    # calculating gradients
    loss.backward()

    # updating weights
    optimizer.step()

    optimizer.zero_grad()

# testing on new data
X = torch.Tensor([[7], [8]])
predicted = model(X)
print(predicted)
