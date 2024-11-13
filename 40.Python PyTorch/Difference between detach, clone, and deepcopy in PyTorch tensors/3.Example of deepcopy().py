import torch
import copy

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = copy.deepcopy(x).detach()  # Manually performing a deepcopy and detaching

y[0] = 10  # Modifying y does not affect x, and y does not require gradients
print("x:", x)  # x remains unchanged
print("y:", y)  # y is independent and does not track gradients
